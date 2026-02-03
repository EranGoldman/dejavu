# DejaVu Documentation

Welcome to the DejaVu documentation!

## Contents

### Getting Started
- [Installation Guide](installation.md)
- [Quick Start](quickstart.md)
- [Architecture Overview](architecture.md)

### Device Setup
- [Raspberry Pi Zero Setup](raspberry-pi-setup.md)
- [ESP32-CAM Setup](esp32-setup.md)
- [Device Configuration](device-config.md)

### Backend
- [API Documentation](api-reference.md)
- [Database Schema](database-schema.md)
- [AI/ML Models](ai-models.md)

### Frontend
- [Dashboard Guide](dashboard-guide.md)
- [Customization](frontend-customization.md)

### Deployment
- [Production Deployment](production-deployment.md)
- [Security Best Practices](security.md)
- [Monitoring and Logging](monitoring.md)

### Development
- [Contributing Guide](../CONTRIBUTING.md)
- [Code Style](code-style.md)
- [Testing Guide](testing-guide.md)

## Project Overview

DejaVu is an open-source wearable visual memory system that:

1. **Captures** - Uses a camera device (Pi Zero or ESP32-CAM) to capture images
2. **Tags** - Automatically tags images using AI/ML models
3. **Stores** - Saves images and metadata in a searchable database
4. **Recalls** - Provides a dashboard to search and browse your visual memories

## Architecture

```
┌─────────────┐      Wi-Fi/HTTP      ┌──────────────┐
│   Device    │ ───────────────────> │   Backend    │
│ (Pi/ESP32)  │                       │  (Flask API) │
└─────────────┘                       └──────┬───────┘
                                             │
                                             │ REST API
                                             │
                                      ┌──────▼───────┐
                                      │   Frontend   │
                                      │  (Dashboard) │
                                      └──────────────┘
```

## Quick Links

- [GitHub Repository](https://github.com/EranGoldman/dejavu)
- [Issue Tracker](https://github.com/EranGoldman/dejavu/issues)
- [Discussions](https://github.com/EranGoldman/dejavu/discussions)

## Support

For questions, issues, or contributions, please visit our GitHub repository or create an issue.
