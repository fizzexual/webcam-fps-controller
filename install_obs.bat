@echo off
echo ============================================================
echo OBS Studio Installer for Virtual Webcam FPS Controller
echo ============================================================
echo.

REM Check if winget is available
winget --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Winget not found. Trying Chocolatey...
    goto :try_choco
)

echo Installing OBS Studio using winget...
echo.
winget install --id OBSProject.OBSStudio -e --silent
if %errorlevel% equ 0 (
    echo.
    echo ============================================================
    echo OBS Studio installed successfully!
    echo ============================================================
    echo.
    echo Please RESTART your computer for the virtual camera driver to work.
    echo After restart, run: python virtual_webcam_fps.py
    echo.
    pause
    exit /b 0
)

:try_choco
REM Check if chocolatey is available
choco --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Neither winget nor chocolatey found.
    goto :manual_install
)

echo Installing OBS Studio using Chocolatey...
echo.
choco install obs-studio -y
if %errorlevel% equ 0 (
    echo.
    echo ============================================================
    echo OBS Studio installed successfully!
    echo ============================================================
    echo.
    echo Please RESTART your computer for the virtual camera driver to work.
    echo After restart, run: python virtual_webcam_fps.py
    echo.
    pause
    exit /b 0
)

:manual_install
echo.
echo ============================================================
echo Automatic installation not available
echo ============================================================
echo.
echo Please install OBS Studio manually:
echo.
echo 1. Opening download page in your browser...
echo 2. Download and run the installer
echo 3. Restart your computer after installation
echo 4. Run: python virtual_webcam_fps.py
echo.
start https://obsproject.com/download
echo.
pause
exit /b 1
