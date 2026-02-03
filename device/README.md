# DejaVu Device

This directory contains the code for the DejaVu device component, designed to run on:
- Raspberry Pi Zero W/WH
- ESP32-CAM

## Overview

The device captures images and uploads them to the backend API when Wi-Fi is available. It includes:
- Image capture functionality
- Wi-Fi connectivity management
- Offline queueing for images
- Secure upload to backend API

## Setup

### Raspberry Pi Zero W

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Configure the device:
   - Copy `.env.example` from root to `.env`
   - Update configuration in `config.py`

3. Run the device:
```bash
python main.py
```

### ESP32-CAM

Refer to the ESP32 specific documentation in `docs/esp32-setup.md`.

## Configuration

Edit `config.py` to customize:
- Camera settings (resolution, quality)
- Upload intervals
- Backend API endpoint
- Wi-Fi credentials (stored in .env)

## File Structure

- `main.py` - Entry point for the device application
- `config.py` - Configuration settings
- `requirements.txt` - Python dependencies
- `camera.py` - Camera interface and capture logic
- `uploader.py` - Upload management and queueing
- `wifi_manager.py` - Wi-Fi connectivity handling
