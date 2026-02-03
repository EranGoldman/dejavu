"""
WiFi Setup Server for DejaVu Device

A simple HTTP server that allows users to connect to the device via IP address
and configure WiFi credentials. This is useful for initial device setup when
the device doesn't have WiFi credentials configured yet.

SECURITY NOTES:
- This server is intended for LOCAL NETWORK use during initial device setup
- Binding to 0.0.0.0 allows access from any device on the same network
- No authentication is required to simplify initial setup
- File permissions are set to 0o600 to protect stored credentials
- Use this server only on trusted networks
- Consider disabling the server after initial WiFi configuration

Usage:
    python wifi_setup_server.py

The server will start on port 8080 and can be accessed via:
    http://<device-ip>:8080
"""
import os
import json
import logging
from pathlib import Path
from flask import Flask, request, render_template_string, jsonify

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__)
# Use environment variable or generate a random secret key
app.config['SECRET_KEY'] = os.getenv('WIFI_SETUP_SECRET_KEY', os.urandom(24).hex())

# Configuration file path
CONFIG_FILE = Path(__file__).parent / 'wifi_credentials.json'

# HTML template for WiFi setup page
SETUP_PAGE_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DejaVu WiFi Setup</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }
        .container {
            background: white;
            border-radius: 12px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
            padding: 40px;
            max-width: 500px;
            width: 100%;
        }
        h1 {
            color: #333;
            margin-bottom: 10px;
            font-size: 28px;
        }
        .subtitle {
            color: #666;
            margin-bottom: 30px;
            font-size: 14px;
        }
        .form-group {
            margin-bottom: 20px;
        }
        label {
            display: block;
            margin-bottom: 8px;
            color: #333;
            font-weight: 500;
            font-size: 14px;
        }
        input[type="text"],
        input[type="password"] {
            width: 100%;
            padding: 12px 16px;
            border: 2px solid #e1e8ed;
            border-radius: 8px;
            font-size: 14px;
            transition: border-color 0.3s;
        }
        input[type="text"]:focus,
        input[type="password"]:focus {
            outline: none;
            border-color: #667eea;
        }
        .btn {
            width: 100%;
            padding: 14px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            border-radius: 8px;
            font-size: 16px;
            font-weight: 600;
            cursor: pointer;
            transition: transform 0.2s, box-shadow 0.2s;
        }
        .btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
        }
        .btn:active {
            transform: translateY(0);
        }
        .btn:disabled {
            opacity: 0.6;
            cursor: not-allowed;
        }
        .message {
            margin-top: 20px;
            padding: 12px;
            border-radius: 8px;
            display: none;
            font-size: 14px;
        }
        .message.success {
            background-color: #d4edda;
            color: #155724;
            border: 1px solid #c3e6cb;
        }
        .message.error {
            background-color: #f8d7da;
            color: #721c24;
            border: 1px solid #f5c6cb;
        }
        .wifi-list {
            margin-bottom: 20px;
            max-height: 200px;
            overflow-y: auto;
        }
        .current-config {
            background: #f8f9fa;
            padding: 15px;
            border-radius: 8px;
            margin-bottom: 20px;
        }
        .current-config h3 {
            font-size: 14px;
            color: #666;
            margin-bottom: 10px;
        }
        .current-config p {
            font-size: 14px;
            color: #333;
            margin: 5px 0;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🧠 DejaVu WiFi Setup</h1>
        <p class="subtitle">Configure WiFi credentials for your device</p>
        
        {% if current_credentials %}
        <div class="current-config">
            <h3>Current Configuration</h3>
            {% for wifi in current_credentials %}
            <p><strong>Network {{ loop.index }}:</strong> {{ wifi.ssid }}</p>
            {% endfor %}
        </div>
        {% endif %}
        
        <form id="wifiForm">
            <div class="form-group">
                <label for="ssid">WiFi Network Name (SSID)</label>
                <input type="text" id="ssid" name="ssid" required placeholder="Enter network name">
            </div>
            
            <div class="form-group">
                <label for="password">WiFi Password</label>
                <input type="password" id="password" name="password" required placeholder="Enter password">
            </div>
            
            <button type="submit" class="btn" id="submitBtn">Save WiFi Credentials</button>
        </form>
        
        <div id="message" class="message"></div>
    </div>
    
    <script>
        document.getElementById('wifiForm').addEventListener('submit', async function(e) {
            e.preventDefault();
            
            const submitBtn = document.getElementById('submitBtn');
            const messageDiv = document.getElementById('message');
            const ssid = document.getElementById('ssid').value;
            const password = document.getElementById('password').value;
            
            // Disable button and show loading state
            submitBtn.disabled = true;
            submitBtn.textContent = 'Saving...';
            messageDiv.style.display = 'none';
            
            try {
                const response = await fetch('/setup', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ ssid, password })
                });
                
                const data = await response.json();
                
                if (response.ok) {
                    messageDiv.className = 'message success';
                    messageDiv.textContent = data.message || 'WiFi credentials saved successfully!';
                    messageDiv.style.display = 'block';
                    
                    // Clear form
                    document.getElementById('wifiForm').reset();
                    
                    // Reload after 2 seconds to show updated config
                    setTimeout(() => {
                        window.location.reload();
                    }, 2000);
                } else {
                    messageDiv.className = 'message error';
                    messageDiv.textContent = data.error || 'Failed to save WiFi credentials';
                    messageDiv.style.display = 'block';
                }
            } catch (error) {
                messageDiv.className = 'message error';
                messageDiv.textContent = 'Network error. Please try again.';
                messageDiv.style.display = 'block';
            } finally {
                submitBtn.disabled = false;
                submitBtn.textContent = 'Save WiFi Credentials';
            }
        });
    </script>
</body>
</html>
"""


def load_wifi_credentials():
    """Load WiFi credentials from configuration file"""
    if CONFIG_FILE.exists():
        try:
            with open(CONFIG_FILE, 'r') as f:
                return json.load(f)
        except Exception as e:
            logger.error(f"Error loading WiFi credentials: {e}")
    return []


def save_wifi_credentials(credentials):
    """Save WiFi credentials to configuration file"""
    try:
        with open(CONFIG_FILE, 'w') as f:
            json.dump(credentials, f, indent=2)
        # Set restrictive file permissions (owner read/write only)
        os.chmod(CONFIG_FILE, 0o600)
        logger.info(f"WiFi credentials saved to {CONFIG_FILE}")
        return True
    except Exception as e:
        logger.error(f"Error saving WiFi credentials: {e}")
        return False


@app.route('/')
def index():
    """Serve the WiFi setup page"""
    credentials = load_wifi_credentials()
    # Only show SSID, not passwords
    safe_credentials = [{'ssid': c.get('ssid', 'Unknown')} for c in credentials]
    return render_template_string(SETUP_PAGE_HTML, current_credentials=safe_credentials)


@app.route('/setup', methods=['POST'])
def setup_wifi():
    """Handle WiFi credential submission"""
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        ssid = data.get('ssid', '').strip()
        password = data.get('password', '').strip()
        
        if not ssid:
            return jsonify({'error': 'WiFi network name (SSID) is required'}), 400
        
        if not password:
            return jsonify({'error': 'WiFi password is required'}), 400
        
        # Load existing credentials
        credentials = load_wifi_credentials()
        
        # Check if SSID already exists and update, otherwise add new
        existing_index = next((i for i, c in enumerate(credentials) if c.get('ssid') == ssid), None)
        
        new_credential = {
            'ssid': ssid,
            'password': password
        }
        
        if existing_index is not None:
            credentials[existing_index] = new_credential
            message = f'WiFi credentials updated for network: {ssid}'
        else:
            credentials.append(new_credential)
            message = f'WiFi credentials added for network: {ssid}'
        
        # Save credentials
        if save_wifi_credentials(credentials):
            logger.info(message)
            return jsonify({
                'success': True,
                'message': message
            }), 200
        else:
            return jsonify({'error': 'Failed to save WiFi credentials'}), 500
            
    except Exception as e:
        logger.error(f"Error in setup_wifi: {e}", exc_info=True)
        return jsonify({'error': 'An error occurred while saving WiFi credentials'}), 500


@app.route('/credentials', methods=['GET'])
def get_credentials():
    """Get list of configured WiFi networks (SSIDs only, no passwords)"""
    credentials = load_wifi_credentials()
    # Return only SSIDs for security
    safe_credentials = [{'ssid': c.get('ssid', 'Unknown')} for c in credentials]
    return jsonify({'credentials': safe_credentials}), 200


@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({'status': 'ok', 'service': 'WiFi Setup Server'}), 200


def main():
    """Main entry point for the WiFi setup server"""
    logger.info("Starting DejaVu WiFi Setup Server")
    logger.info(f"Configuration file: {CONFIG_FILE}")
    logger.info("SECURITY: This server is for local network use during device setup")
    
    # Get host and port from environment or use defaults
    host = os.getenv('WIFI_SETUP_HOST', '0.0.0.0')
    port = int(os.getenv('WIFI_SETUP_PORT', 8080))
    
    logger.info(f"Server will be accessible at http://{host}:{port}")
    logger.info("Access the setup page from any device on the same network")
    logger.warning("WARNING: No authentication required - use only on trusted networks")
    
    # Run the Flask app (development server - suitable for device setup use case)
    app.run(host=host, port=port, debug=False)


if __name__ == '__main__':
    main()
