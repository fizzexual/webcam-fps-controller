@echo off
echo ============================================================
echo Virtual Webcam FPS Controller
echo ============================================================
echo.

:: Check if Python is installed
python --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Python is not installed!
    echo Download from: https://www.python.org/downloads/
    echo.
    pause
    exit /b 1
)

:: Check if requirements are installed
echo Checking dependencies...
python -c "import cv2, pyvirtualcam, keyboard" >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo Installing dependencies...
    pip install -r requirements.txt
    if %ERRORLEVEL% NEQ 0 (
        echo.
        echo ERROR: Failed to install dependencies
        echo.
        pause
        exit /b 1
    )
)

echo.
echo Starting virtual webcam...
echo Keep this window open!
echo.
echo Controls:
echo   + or =       : Increase FPS by 1
echo   -            : Decrease FPS by 1
echo   P            : Toggle preview
echo   Q            : Quit (when preview is on)
echo   Ctrl+Q+P     : Quit (when preview is off)
echo   Ctrl+Shift+P : Show preview (when preview is off)
echo.
echo ============================================================
echo.

python virtual_webcam_fps.py

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ============================================================
    echo ERROR: Failed to start
    echo ============================================================
    echo.
    echo Install OBS Studio: https://obsproject.com/download
    echo Then run this again.
    echo.
    pause
)
