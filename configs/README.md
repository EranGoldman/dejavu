# DejaVu Configuration Files

This directory contains shared configuration files for the DejaVu project.

## Files

### `devices.yml`
Configuration for registered devices. Example:
```yaml
devices:
  - id: dejavu-001
    name: "Pi Zero - Living Room"
    type: raspberry-pi-zero-w
    capture_interval: 30
    
  - id: dejavu-002
    name: "ESP32-CAM - Entrance"
    type: esp32-cam
    capture_interval: 60
```

### `ai-models.yml`
Configuration for AI/ML models used for tagging:
```yaml
models:
  image_classification:
    name: "clip-vit-base-patch32"
    enabled: true
    confidence_threshold: 0.7
    
  object_detection:
    name: "yolov8n"
    enabled: true
    confidence_threshold: 0.5
```

### `nginx.conf`
Sample Nginx configuration for production deployment.

### `systemd/`
Systemd service files for running DejaVu components as services.

## Usage

### Development
Copy example configurations and customize:
```bash
cp configs/devices.yml.example configs/devices.yml
# Edit configs/devices.yml with your settings
```

### Production
Use these configurations as templates for your production deployment:
```bash
# Copy systemd service
sudo cp configs/systemd/dejavu-backend.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable dejavu-backend
sudo systemctl start dejavu-backend
```

## Configuration Hierarchy

1. **Environment Variables** (highest priority)
   - Set via `.env` file or system environment
   
2. **Config Files** (medium priority)
   - YAML files in this directory
   
3. **Code Defaults** (lowest priority)
   - Default values in `config.py` files

## Security Note

⚠️ **Never commit sensitive data** like API keys, passwords, or tokens to this directory. Use environment variables or `.env` files (which should be in `.gitignore`).
