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
# 🧠 DejaVu — Personal Visual Memory Assistant

DejaVu is an open‑source project that combines a wearable camera device and an intelligent backend to help users recall daily visual moments. The system continuously captures images, tags them with semantic labels, and enables natural‑language search such as _“When did I last see my keys?”_ or _“Did I close the front door?”_

---

## 🌐 Architecture Overview

**DejaVu** consists of two main components:

### 1. Edge Device (Wearable)
- Runs on Raspberry Pi Zero 2 W or ESP32‑CAM  
- Captures images every 1–2 seconds  
- Stores images locally (SD card)  
- Automatically uploads when connected to a trusted Wi‑Fi network  

### 2. Backend (Flask API)
- Receives uploaded images from the device  
- Uses vision models (e.g., CLIP, TensorFlow, OpenAI API) to tag images  
- Stores metadata (timestamp, objects, location)  
- Supports natural‑language search for object recall  
- Optionally exposes a lightweight web interface or API for queries  

**Optional Components**
- `frontend/` – Simple web UI to visualize images and search results  
- `ai/` – Local or remote image labeling and semantic embedding services  

---

## 🧩 Project Structure

```
dejavu/
├── device/                # Wearable edge code (Pi Zero / ESP32)
│   ├── capture.py
│   ├── uploader.py
│   └── config/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   ├── models.py
│   │   └── vision.py
│   ├── db/
│   │   └── schema.sql
│   ├── tests/
│   │   └── test_api.py
│   └── Dockerfile
├── frontend/
│   ├── index.html
│   └── js/
│       └── main.js
├── docs/
│   └── architecture.md
├── docker-compose.yml
├── requirements.txt
├── .env.example
├── LICENSE
└── README.md
```

---

## ⚙️ Deployment (Docker Compose)

```bash
git clone https://github.com/EranGoldman/dejavu.git
cd dejavu
cp .env.example .env
docker compose up --build
```

**Services:**
- `flask` – API Server (Port 5000)  
- `db` – PostgreSQL/SQLite  
- `vision` – Optional image tagging microservice  

---

## 👨‍💻 Contribution Guide

1. Fork the repository  
2. Create a feature branch  
3. Commit changes with clear messages  
4. Open a Pull Request  

Before submitting:
- Ensure code passes linting/tests  
- Update documentation in `/docs`  
- Provide descriptive PR comments  

---

## 🧠 Roadmap

- [ ] Object and facial recognition  
- [ ] Natural‑language question parser  
- [ ] Mobile dashboard  
- [ ] Encrypted local storage  

---

## 📜 License

This project is licensed under the **Apache License 2.0**.  
Full text in [`LICENSE`](./LICENSE).

```
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   https://www.apache.org/licenses/LICENSE-2.0
```

---

## ⚖️ Disclaimer

This project was **conceptualized and written by a human developer**, with text formatting and documentation **edited and refined by AI assistance**.  
All code and original content remain human‑authored and community‑maintained.

---

## 💡 Acknowledgments

- Inspired by lifelogging and quantified‑self projects  
- Uses open‑source vision & Flask ecosystem  
- Privacy‑focused and locally deployable  

---

## 🚀 Quick Links

- **Docs:** [`/docs/architecture.md`](./docs/architecture.md)  
- **Issues:** [GitHub Issues](https://github.com/EranGoldman/dejavu/issues)  
- **License:** [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0)
```


