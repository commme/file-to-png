"""
file-to-png converter
  - PDF  → PNG  (PyMuPDF, 의존성 없음)
  - HWP  → PNG  (LibreOffice 필요)

사용법:
  py convert.py                  # input/ 폴더 자동 처리
  py convert.py 파일.pdf         # 파일 직접 지정
  py convert.py 파일.hwp 파일.pdf  # 여러 파일
"""

import sys
import os
import subprocess
import shutil
from pathlib import Path

# Windows 터미널 UTF-8 출력 강제
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

BASE_DIR = Path(__file__).parent
INPUT_DIR = BASE_DIR / "input"
OUTPUT_DIR = BASE_DIR / "output"
OUTPUT_DIR.mkdir(exist_ok=True)

# LibreOffice 경로 (설치 안 된 경우 None)
SOFFICE_PATHS = [
    "C:/Program Files/LibreOffice/program/soffice.exe",
    "C:/Program Files (x86)/LibreOffice/program/soffice.exe",
]
SOFFICE = next((p for p in SOFFICE_PATHS if Path(p).exists()), None)


def pdf_to_png(pdf_path: Path, out_dir: Path, dpi: int = 200):
    """PDF 각 페이지를 PNG로 변환 (pypdfium2 사용)"""
    try:
        import pypdfium2 as pdfium
    except ImportError:
        print("  [오류] pypdfium2 미설치: py -m pip install pypdfium2")
        return False

    doc = pdfium.PdfDocument(str(pdf_path))
    stem = pdf_path.stem
    total = len(doc)
    scale = dpi / 72

    for i, page in enumerate(doc):
        bitmap = page.render(scale=scale, rotation=0)
        pil_img = bitmap.to_pil()
        if total == 1:
            out_path = out_dir / f"{stem}.png"
        else:
            out_path = out_dir / f"{stem}_p{i+1:03d}.png"
        pil_img.save(str(out_path))
        print(f"  ✓ {out_path.name}")

    doc.close()
    return True


def hwp_to_png(hwp_path: Path, out_dir: Path):
    """HWP → PDF(LibreOffice) → PNG"""
    if not SOFFICE:
        print("  [오류] LibreOffice 미설치")
        print("  설치: https://www.libreoffice.org/download/download/")
        return False

    # 임시 폴더에 PDF 생성
    tmp_dir = BASE_DIR / "_tmp"
    tmp_dir.mkdir(exist_ok=True)

    result = subprocess.run(
        [SOFFICE, "--headless", "--convert-to", "pdf",
         "--outdir", str(tmp_dir), str(hwp_path)],
        capture_output=True, text=True
    )

    pdf_path = tmp_dir / (hwp_path.stem + ".pdf")
    if not pdf_path.exists():
        print(f"  [오류] PDF 변환 실패: {result.stderr.strip()}")
        return False

    ok = pdf_to_png(pdf_path, out_dir)
    pdf_path.unlink(missing_ok=True)
    if not any(tmp_dir.iterdir()):
        tmp_dir.rmdir()
    return ok


def process(file_path: Path):
    ext = file_path.suffix.lower()
    print(f"\n[처리] {file_path.name}")

    if ext == ".pdf":
        pdf_to_png(file_path, OUTPUT_DIR)
    elif ext in (".hwp", ".hwpx"):
        hwp_to_png(file_path, OUTPUT_DIR)
    else:
        print(f"  [건너뜀] 지원 형식: .pdf .hwp .hwpx")


def main():
    targets = []

    if len(sys.argv) > 1:
        # 직접 파일 지정
        for arg in sys.argv[1:]:
            p = Path(arg)
            if p.exists():
                targets.append(p)
            else:
                print(f"[없음] {arg}")
    else:
        # input/ 폴더 자동 스캔
        if not INPUT_DIR.exists():
            INPUT_DIR.mkdir()
        targets = [f for f in INPUT_DIR.iterdir()
                   if f.suffix.lower() in (".pdf", ".hwp", ".hwpx")]
        if not targets:
            print(f"input/ 폴더에 PDF 또는 HWP 파일을 넣고 다시 실행하세요.")
            print(f"  위치: {INPUT_DIR}")
            return

    for t in targets:
        process(t)

    print(f"\n완료 → {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
