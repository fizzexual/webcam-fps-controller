# 🎥 Virtual Webcam FPS Controller 🍂

Control your webcam's frame rate in real-time for Discord, Zoom, Teams, and any video app.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.7+-blue.svg)
![Platform](https://img.shields.io/badge/platform-windows-lightgrey.svg)

## About

A single Python script (about 150 lines) for Windows users who want to send a lower or fixed webcam frame rate to Discord, Zoom or Teams, for example to save bandwidth or CPU. It reads the webcam with OpenCV and re-publishes it through the OBS Virtual Camera driver (via pyvirtualcam) at the FPS you set from the keyboard. It is a small working utility with no packaged release; `run.bat` is the launcher.

## ✨ Features

- 🎮 **Real-time FPS control** - Adjust from 1-60 FPS on the fly
- 📹 **Works everywhere** - Discord, Zoom, Teams, OBS, any app
- 🖥️ **Live preview** - See what others see with FPS overlay
- ⚡ **Lightweight** - Minimal resource usage
- 🎯 **Simple controls** - Just +/- keys to adjust

## 🚀 Quick Start

### Prerequisites

- Python 3.7+
- [OBS Studio](https://obsproject.com/download) (for virtual camera driver)

### Installation

1. **Install OBS Studio**
   ```
   Download from: https://obsproject.com/download
   ```
   *(You don't need to open OBS, just have it installed)*

2. **Run the script**
   ```bash
   run.bat
   ```
   The batch file will automatically install Python dependencies and start the virtual camera.

3. **Select camera in your app**
   - **Discord**: Settings → Voice & Video → Camera → "OBS Virtual Camera"
   - **Zoom**: Settings → Video → "OBS Virtual Camera"
   - **Teams**: Settings → Devices → Camera → "OBS Virtual Camera"

## 🎮 Controls

| Key | Action |
|-----|--------|
| `+` or `=` | Increase FPS by 1 |
| `-` | Decrease FPS by 1 |
| `P` | Toggle preview window |
| `Q` | Quit (when preview is on) |
| `Ctrl+Q+P` | Quit (when preview is off) |
| `Ctrl+Shift+P` | Show preview (when preview is off) |

## ⚙️ Configuration

Edit `virtual_webcam_fps.py` to customize:

```python
controller = VirtualWebcamFPS(
    camera_index=0,    # 0 = default webcam, 1 = second webcam
    target_fps=30,     # Starting FPS (1-60)
    width=1280,        # Resolution width
    height=720         # Resolution height
)
```

### Common Resolutions

- `640x480` - SD
- `1280x720` - HD (default)
- `1920x1080` - Full HD

## 🔧 Troubleshooting

<details>
<summary><b>"Virtual Camera Not Available" error</b></summary>

- Install OBS Studio from https://obsproject.com/download
- Restart your computer after installation
- Run `run.bat` again
</details>

<details>
<summary><b>"Cannot open camera" error</b></summary>

- Close other apps using your webcam (Zoom, Teams, etc.)
- Try changing `camera_index` to `1` or `2` in the script
- Check if your webcam is properly connected
</details>

<details>
<summary><b>Camera not showing in Discord</b></summary>

- Make sure `run.bat` is running (keep the window open)
- Restart Discord
- Check Discord Settings → Voice & Video → Camera
</details>

## 📋 Requirements

```
opencv-python==4.8.1.78
pyvirtualcam==0.11.0
keyboard==0.13.5
```

## 🐧 Linux Support

On Linux, use v4l2loopback instead of OBS:

```bash
# Install v4l2loopback
sudo apt install v4l2loopback-dkms

# Load the module
sudo modprobe v4l2loopback devices=1 video_nr=42 card_label="VirtualCam"

# Install Python dependencies
pip install -r requirements.txt

# Run the script
python virtual_webcam_fps.py
```

## 📝 License

MIT License - feel free to use and modify!

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

## ⭐ Show your support

Give a ⭐️ if this project helped you!
