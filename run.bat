@echo off
chcp 65001 > nul
echo ===========================
echo  PDF / HWP → PNG 변환기
echo ===========================
echo.
echo input\ 폴더에 파일 넣고 아무 키나 누르세요...
pause > nul
py "%~dp0convert.py"
echo.
pause
