# DejaVu Frontend

Simple dashboard for viewing and searching captured images.

## Overview

The frontend provides:
- Image gallery view
- Search functionality
- Tag-based filtering
- Image timeline
- Device status monitoring

## Setup

### Development

Simply open `index.html` in a web browser, or use a local server:

```bash
# Using Python
python -m http.server 8000

# Using Node.js
npx serve .
```

Then navigate to `http://localhost:8000`

### Configuration

Update the API endpoint in `index.html` to point to your backend:
```javascript
const API_URL = 'http://localhost:5000';
```

## Features

- **Gallery View**: Browse all captured images
- **Search**: Full-text search across tags and metadata
- **Timeline**: View images chronologically
- **Filters**: Filter by date, device, or tags
- **Responsive Design**: Works on desktop and mobile

## File Structure

- `index.html` - Main dashboard page
- `style.css` - Styling (optional)
- `script.js` - JavaScript functionality (optional)

## Technology Stack

- Pure HTML/CSS/JavaScript (no build process required)
- Can be enhanced with frameworks like React, Vue, or Svelte
