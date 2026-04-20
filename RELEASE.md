# File to PNG 🖼️

**PDF·HWP 파일을 PNG 이미지로 한 방에. 브라우저에서 드래그만 하면 끝.**

🔗 바로 쓰기: **https://commme.github.io/file-to-png/**

---

## 이런 분께

- PDF 한 장만 카톡/슬랙에 이미지로 던지고 싶다
- 회의 자료 PDF를 썸네일로 미리 보여주고 싶다
- HWP 파일을 카드뉴스용 이미지로 바꿔야 한다
- 폴더 안 PDF 수십 개를 한꺼번에 PNG로 뽑고 싶다
- 온라인 변환기는 파일이 외부로 나가서 찜찜하다

---

## 30초 요약

**브라우저 버전 (PDF만)**
1. https://commme.github.io/file-to-png/ 접속
2. PDF 드래그
3. PNG 자동 다운로드 끝

**Python 버전 (PDF + HWP + 일괄)**
1. `pip install pypdfium2 Pillow`
2. `input/` 폴더에 파일 넣기
3. `python convert.py` → `output/`에 PNG 쏟아짐

데이터는 **전부 본인 PC에서만** 처리됨.

---

## 시작하기

### 방법 1: 브라우저 (제일 간편)

```
https://commme.github.io/file-to-png/
→ PDF 드래그
→ 페이지별 PNG 자동 다운로드
```

설치 ❌ 로그인 ❌ 인터넷만 있으면 됨.

### 방법 2: Python (HWP까지 + 일괄)

```bash
# 의존성 (최초 1회)
pip install pypdfium2 Pillow

# input/ 폴더에 파일 넣고
python convert.py

# 또는 개별 파일
python convert.py 보고서.pdf 한글파일.hwp
```

HWP 변환만 [LibreOffice](https://www.libreoffice.org/download/download/) 필요.

### 방법 3: Windows 더블클릭

`run.bat` 더블클릭 → 안내대로 `input/` 폴더에 파일 → 자동 변환.

---

## 무엇이 변환되나

| 입력 | 출력 | 도구 |
|------|------|------|
| PDF (브라우저) | 페이지별 PNG | PDF.js |
| PDF (Python) | 페이지별 PNG | pypdfium2 |
| HWP (Python) | PDF → PNG | LibreOffice + pypdfium2 |

---

## 자주 묻는 질문

**Q. 파일이 외부로 나가요?** **아니요.** 브라우저 버전은 PDF.js가 로컬에서 렌더링, Python 버전은 완전 오프라인.

**Q. 페이지가 많은 PDF는 시간 얼마나?** 100페이지 기준 약 30초 내외 (PC 사양에 따라 다름).

**Q. 해상도 조절 돼요?** Python 버전은 `convert.py` 내 scale 인자로 조절. 브라우저는 기본 2x 렌더링.

**Q. HWP가 브라우저에선 왜 안 돼요?** 한컴 포맷 디코더가 무거워서 Python + LibreOffice로만 지원.

**Q. 모바일에서도 돼요?** 브라우저 버전은 됨. 단 큰 PDF는 메모리 한계.

**Q. 결과 PNG가 흐려요.** Python 버전에서 `scale=4` 정도로 올리면 또렷해짐 (파일 크기 ↑).

---

## 보안·개인정보

| 항목 | 상태 |
|------|------|
| 로그인/계정 | ❌ 없음 |
| 파일 외부 전송 | ❌ 전혀 없음 |
| 변환 위치 | 브라우저(로컬) 또는 본인 PC |
| 외부 스크립트 | CSP로 차단, PDF.js만 허용 |
| XSS 방지 | 파일명 textContent 처리 |
| 결과물 보존 | Python: `output/` 폴더 / 브라우저: 다운로드 폴더 |

### ⚠️ 공용 PC에서 쓸 때

브라우저 버전은 다운로드 폴더에 PNG가 그대로 남습니다. 사용 후 폴더 정리하고 나오세요.

---

## 단축 기능

- 브라우저: 다중 PDF 드래그 가능
- Python: `input/` 폴더 통째로 일괄 변환
- 페이지별 파일명 자동 부여 (`보고서_p001.png`, `_p002.png`...)

---

## 만든 사람

© 2026 COMMME · 오픈소스

피드백/버그: https://github.com/commme/file-to-png/issues
