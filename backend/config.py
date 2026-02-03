"""
Configuration settings for DejaVu backend
"""
import os
from dotenv import load_dotenv

load_dotenv()

# Flask Configuration
SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')
DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'

# Database Configuration
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///dejavu.db')
SQLALCHEMY_DATABASE_URI = DATABASE_URL
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Storage Configuration
UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER', './uploads')
MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# API Configuration
API_KEY = os.getenv('API_KEY', '')
REQUIRE_API_KEY = os.getenv('REQUIRE_API_KEY', 'False').lower() == 'true'

# AI/ML Configuration
AI_MODEL = os.getenv('AI_MODEL', 'clip-vit-base-patch32')
USE_GPU = os.getenv('USE_GPU', 'False').lower() == 'true'

# CORS Configuration
CORS_ORIGINS = os.getenv('CORS_ORIGINS', '*').split(',')
