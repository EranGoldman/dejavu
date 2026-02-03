# DejaVu Backend

Flask API for tagging, storing, and searching images from DejaVu devices.

## Overview

The backend provides:
- RESTful API for image upload and retrieval
- Automatic image tagging using AI/ML
- Full-text search capabilities
- Image storage and management
- Device authentication and authorization

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Configure the application:
   - Copy `.env.example` from root to `.env`
   - Update database credentials
   - Set API keys for AI services

3. Initialize the database:
```bash
python -c "from app import db; db.create_all()"
```

4. Run the development server:
```bash
python app.py
```

Or use Flask CLI:
```bash
flask run
```

## Production Deployment

For production, use a WSGI server like Gunicorn:
```bash
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

## API Endpoints

### Images
- `POST /api/images` - Upload a new image
- `GET /api/images` - List all images
- `GET /api/images/<id>` - Get specific image
- `DELETE /api/images/<id>` - Delete an image

### Search
- `GET /api/search?q=<query>` - Search images by tags or metadata

### Tags
- `GET /api/tags` - List all tags
- `GET /api/tags/<tag>/images` - Get images with specific tag

## Configuration

Edit `config.py` to customize:
- Database connection
- Storage backend (local/S3)
- AI/ML model settings
- API authentication
