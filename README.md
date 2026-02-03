# 🧠 DejaVu

DejaVu: an open-source wearable visual memory system that captures, tags, and helps you recall what you've seen.

## Overview

DejaVu is a complete solution for capturing and organizing your visual experiences. It consists of:

- **Device Component**: Runs on Raspberry Pi Zero or ESP32-CAM to capture images
- **Backend API**: Flask-based API for image storage, AI-powered tagging, and search
- **Frontend Dashboard**: Simple web interface to browse and search your visual memories

## Features

- 📸 **Automatic Image Capture**: Capture images at configurable intervals
- 🏷️ **AI-Powered Tagging**: Automatically tag images using machine learning
- 🔍 **Smart Search**: Full-text search across tags and metadata
- 📡 **Offline Support**: Queue images when Wi-Fi is unavailable
- 🌐 **Web Dashboard**: Browse and search images from any device
- 🔒 **Privacy-Focused**: Self-hosted solution - you own your data

## Quick Start

### Prerequisites

- Python 3.8 or higher
- Raspberry Pi Zero W/WH or ESP32-CAM (for device component)
- 4GB+ storage for images

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/EranGoldman/dejavu.git
   cd dejavu
   ```

2. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Running the Backend

```bash
cd backend
pip install -r requirements.txt
python app.py
```

The API will be available at `http://localhost:5000`

### Running the Device

```bash
cd device
pip install -r requirements.txt
python main.py
```

### Accessing the Dashboard

Open `frontend/index.html` in your browser, or serve it with:
```bash
cd frontend
python -m http.server 8000
```

Then navigate to `http://localhost:8000`

## Project Structure

```
dejavu/
├── device/              # Device code (Pi Zero/ESP32-CAM)
│   ├── main.py          # Entry point
│   ├── config.py        # Configuration
│   └── requirements.txt # Device dependencies
├── backend/             # Flask API backend
│   ├── app.py           # Flask application
│   ├── config.py        # Backend configuration
│   └── requirements.txt # Backend dependencies
├── frontend/            # Web dashboard
│   └── index.html       # Dashboard UI
├── docs/                # Documentation
├── tests/               # Test suites
├── configs/             # Shared configurations
├── requirements.txt     # Common dependencies
├── .env.example         # Environment template
├── LICENSE              # MIT License
└── README.md            # This file
```

## Documentation

Comprehensive documentation is available in the [`docs/`](docs/) directory:

- [Installation Guide](docs/installation.md)
- [API Reference](docs/api-reference.md)
- [Device Setup](docs/raspberry-pi-setup.md)
- [Architecture Overview](docs/architecture.md)

## Development

### Running Tests

```bash
pytest tests/
```

### Code Formatting

```bash
black .
flake8 .
```

## Contributing

Contributions are welcome! Please read our [Contributing Guide](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with Flask, Python, and modern web technologies
- AI/ML powered by Hugging Face Transformers
- Designed for privacy and self-hosting

## Support

- 📖 [Documentation](docs/)
- 🐛 [Issue Tracker](https://github.com/EranGoldman/dejavu/issues)
- 💬 [Discussions](https://github.com/EranGoldman/dejavu/discussions)

## Roadmap

- [ ] Enhanced AI tagging models
- [ ] Mobile app for iOS/Android
- [ ] Cloud sync option
- [ ] Video capture support
- [ ] Multi-user support
- [ ] Advanced search filters

---

Made with ❤️ by the DejaVu community
