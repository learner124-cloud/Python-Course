@echo off
REM ============================================================
REM  Ali's Python Course - local preview
REM  DOUBLE-CLICK THIS FILE to start the site on your own PC.
REM
REM  This runs entirely outside any agent session, so the site
REM  stays up until you close the window yourself.
REM ============================================================

setlocal enabledelayedexpansion
set "SITE=%~dp0site"

echo.
echo   ============================================
echo    Ali's Python Course - local preview
echo   ============================================
echo.

if not exist "%SITE%\index.html" (
  echo   ERROR: could not find the site folder:
  echo   %SITE%
  echo.
  echo   Run this file from inside the "Python Course" folder.
  echo.
  pause
  exit /b 1
)

REM ---- find a working Python ----
set "PY="
set "CANDIDATE=C:\Users\Ruhul\.workbuddy-ai\binaries\python\envs\default\Scripts\python.exe"
if exist "!CANDIDATE!" set "PY=!CANDIDATE!"

if not defined PY (
  where python >nul 2>&1 && set "PY=python"
)

if not defined PY (
  echo   ERROR: no Python interpreter found.
  echo.
  echo   Install Python from https://python.org and try again.
  echo.
  pause
  exit /b 1
)

REM ---- is something already listening on 8000? ----
set "PORT=8000"
netstat -an | findstr /r /c:"127.0.0.1:8000 .*LISTENING" >nul 2>&1
if not errorlevel 1 (
  echo   NOTE: port 8000 is already in use.
  echo         The course is very likely ALREADY running.
  echo.
  echo         Opening the browser to it now...
  start "" "http://127.0.0.1:8000/"
  echo.
  echo         If you see a connection error instead, close
  echo         whatever is using port 8000 and run this again.
  echo.
  pause
  exit /b 0
)

echo   Server starting on  http://127.0.0.1:8000
echo.
echo   Opening your browser in a moment...
echo.
echo   --------------------------------------------------
echo    KEEP THIS WINDOW OPEN while you use the course.
echo    Closing it, or pressing Ctrl+C, stops the server.
echo   --------------------------------------------------
echo.

cd /d "%SITE%"

REM open the browser a couple of seconds after the server boots
start "" /b cmd /c "timeout /t 2 >nul & start "" http://127.0.0.1:8000/"

"%PY%" -m http.server 8000 --bind 127.0.0.1

echo.
echo   Server stopped.
echo.
pause
endlocal
