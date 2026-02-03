"""
DejaVu Device - Main Entry Point

Captures images and uploads them to the backend when Wi-Fi is available.
"""
import time
import logging
from pathlib import Path

import config

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def main():
    """Main application loop"""
    logger.info(f"Starting DejaVu Device: {config.DEVICE_NAME}")
    logger.info(f"Device ID: {config.DEVICE_ID}")
    logger.info(f"Backend URL: {config.BACKEND_URL}")
    
    # Create image queue directory if it doesn't exist
    Path(config.IMAGE_QUEUE_DIR).mkdir(parents=True, exist_ok=True)
    
    logger.info("Device initialized successfully")
    logger.info("Ready to capture and upload images")
    
    # Main loop placeholder
    try:
        while True:
            logger.info("Device running... (image capture not yet implemented)")
            time.sleep(config.CAPTURE_INTERVAL)
            
    except KeyboardInterrupt:
        logger.info("Shutting down DejaVu Device")
    except Exception as e:
        logger.error(f"Fatal error: {e}", exc_info=True)


if __name__ == "__main__":
    main()
