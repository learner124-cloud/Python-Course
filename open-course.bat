@echo off
REM ============================================================
REM  Start Ali's Python Course in your browser (local preview)
REM  Just double-click this file.
REM ============================================================

setlocal
set "SITE=%~dp0site"
set "PY=C:\Users\Ruhul\.workbuddy-ai\binaries\python\envs\default\Scripts\python.exe"

if not exist "%SITE%\index.html" (
  echo.
  echo   ERROR: could not find the site folder:
  echo   %SITE%
  echo.
  pause
  exit /b 1
)

if not exist "%PY%" (
  set "PY=python"
)

echo.
echo   ============================================
echo    Ali's Python Course - local preview
echo   ============================================
echo.
echo    Starting server on http://127.0.0.1:8000
echo.
echo    A browser tab will open in a moment.
echo.
echo    KEEP THIS WINDOW OPEN while you browse.
echo    Close this window (or press Ctrl+C) to stop.
echo.

cd /d "%SITE%"

REM open the browser a moment after the server boots
start "" /b cmd /c "timeout /t 2 >nul & start "" http://127.0.0.1:8000/"

"%PY%" -m http.server 8000 --bind 127.0.0.1

echo.
echo   Server stopped.
pause
endlocal
