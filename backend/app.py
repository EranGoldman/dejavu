"""
DejaVu Backend - Flask API Application

Provides REST API for image storage, tagging, and search.
"""
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from pathlib import Path
import logging

import config

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(config)

# Initialize extensions
CORS(app, origins=config.CORS_ORIGINS)
db = SQLAlchemy(app)

# Setup logging
logging.basicConfig(
    level=logging.DEBUG if config.DEBUG else logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


# Database Models
class Image(db.Model):
    """Image model for storing uploaded images"""
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(255), nullable=False)
    device_id = db.Column(db.String(100))
    timestamp = db.Column(db.DateTime, nullable=False)
    tags = db.Column(db.Text)  # JSON array of tags
    metadata = db.Column(db.Text)  # JSON metadata
    
    def to_dict(self):
        return {
            'id': self.id,
            'filename': self.filename,
            'device_id': self.device_id,
            'timestamp': self.timestamp.isoformat(),
            'tags': self.tags,
            'metadata': self.metadata
        }


# Routes
@app.route('/')
def index():
    """API root endpoint"""
    return jsonify({
        'message': 'DejaVu Backend API',
        'version': '1.0.0',
        'endpoints': {
            'images': '/api/images',
            'search': '/api/search',
            'tags': '/api/tags'
        }
    })


@app.route('/api/health')
def health():
    """Health check endpoint"""
    return jsonify({'status': 'healthy'})


@app.route('/api/images', methods=['GET', 'POST'])
def images():
    """Handle image listing and upload"""
    if request.method == 'GET':
        # List all images
        all_images = Image.query.all()
        return jsonify([img.to_dict() for img in all_images])
    
    elif request.method == 'POST':
        # Upload new image (placeholder)
        return jsonify({'message': 'Image upload not yet implemented'}), 501


@app.route('/api/search')
def search():
    """Search images by query"""
    query = request.args.get('q', '')
    return jsonify({
        'query': query,
        'results': [],
        'message': 'Search not yet implemented'
    })


@app.route('/api/tags')
def tags():
    """List all tags"""
    return jsonify({
        'tags': [],
        'message': 'Tag listing not yet implemented'
    })


# Create upload directory
Path(config.UPLOAD_FOLDER).mkdir(parents=True, exist_ok=True)


if __name__ == '__main__':
    # Create database tables
    with app.app_context():
        db.create_all()
    
    logger.info("Starting DejaVu Backend API")
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=config.DEBUG
    )
