"""
Configuration settings for DejaVu device
"""
import os
from dotenv import load_dotenv

load_dotenv()

# Backend API Configuration
BACKEND_URL = os.getenv('BACKEND_URL', 'http://localhost:5000')
API_KEY = os.getenv('API_KEY', '')

# Camera Configuration
CAMERA_RESOLUTION = (1920, 1080)  # Width x Height
CAMERA_QUALITY = 85  # JPEG quality (0-100)
CAPTURE_INTERVAL = 30  # Seconds between captures

# Wi-Fi Configuration
WIFI_CHECK_INTERVAL = 10  # Seconds between Wi-Fi status checks
WIFI_RECONNECT_ATTEMPTS = 3

# Storage Configuration
IMAGE_QUEUE_DIR = os.getenv('IMAGE_QUEUE_DIR', './image_queue')
MAX_QUEUE_SIZE = 1000  # Maximum number of images to store locally

# Device Identification
DEVICE_ID = os.getenv('DEVICE_ID', 'dejavu-device-001')
DEVICE_NAME = os.getenv('DEVICE_NAME', 'DejaVu Device')
