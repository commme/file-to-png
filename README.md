# file-to-png

PDF / HWP 파일을 PNG 이미지로 변환하는 도구. 브라우저 버전과 Python CLI 버전 두 가지를 제공.

## 결과물

- **`converter.html`** — 브라우저에서 드래그 앤 드롭으로 PDF → PNG 변환 (다크 모드 UI)
- **`convert.py`** — 폴더 일괄 변환 Python 스크립트 (PDF + HWP 지원)
- **`run.bat`** — Windows 더블클릭 실행

## 사용법

### 1) 브라우저 (간편)

```
converter.html을 더블클릭 → PDF 파일 드래그 → PNG 자동 다운로드
```

설치 불필요, 인터넷 연결만 있으면 됨 (PDF.js CDN 로드).

### 2) Python (일괄 + HWP 지원)

```bash
# 의존성 설치 (최초 1회)
pip install pypdfium2 Pillow

# input/ 폴더에 파일 넣고 실행
python convert.py

# 또는 개별 파일 지정
python convert.py 파일.pdf 파일.hwp
```

HWP 변환은 [LibreOffice](https://www.libreoffice.org/download/download/) 필요.

### 3) Windows (더블클릭)

`run.bat` 실행 → `input/` 폴더 안내 → 자동 변환.

## 사용된 도구

| 영역 | 라이브러리/도구 |
|------|-----------------|
| 브라우저 PDF 렌더링 | PDF.js 4.0.379 (Mozilla) |
| Python PDF 변환 | pypdfium2 + Pillow |
| HWP → PDF | LibreOffice headless |
| UI 폰트 | Pretendard |

## 보안

- 모든 변환은 **로컬에서만 실행** — 파일이 외부로 전송되지 않음
- CSP 메타 태그로 외부 스크립트 차단
- 파일명은 DOM textContent로 처리 (XSS 방지)

## 라이선스

© 2026 COMMME. All rights reserved.
