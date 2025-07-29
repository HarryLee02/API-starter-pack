from flask import Flask, render_template_string, send_file
import os
from datetime import datetime

app = Flask(__name__)

# HTML template for the logs page
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Scraper Logs</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        .log-section { margin: 20px 0; }
        .log-content { 
            background: #f5f5f5; 
            padding: 15px; 
            border-radius: 5px; 
            white-space: pre-wrap; 
            font-family: monospace;
            max-height: 500px;
            overflow-y: auto;
        }
        .timestamp { color: #666; font-size: 12px; }
        .download-link { 
            display: inline-block; 
            margin: 10px 0; 
            padding: 10px 20px; 
            background: #007bff; 
            color: white; 
            text-decoration: none; 
            border-radius: 5px; 
        }
        .download-link:hover { background: #0056b3; }
    </style>
</head>
<body>
    <h1>Help Center Scraper Logs</h1>
    <p class="timestamp">Last updated: {{ timestamp }}</p>
    
    <div class="log-section">
        <h2>Latest Scraper Log</h2>
        <a href="/download/scraper.log" class="download-link">Download Log File</a>
        <div class="log-content">{{ scraper_log }}</div>
    </div>
    
    <div class="log-section">
        <h2>Available Log Files</h2>
        <ul>
        {% for log_file in log_files %}
            <li><a href="/download/{{ log_file }}">{{ log_file }}</a></li>
        {% endfor %}
        </ul>
    </div>
</body>
</html>
"""

@app.route('/')
def logs():
    """Main logs page"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Read scraper log
    scraper_log = "No log file found"
    if os.path.exists('./logs/scraper.log'):
        try:
            with open('./logs/scraper.log', 'r') as f:
                scraper_log = f.read()
        except:
            scraper_log = "Error reading log file"
    
    # Get list of all log files
    log_files = []
    if os.path.exists('./logs'):
        log_files = [f for f in os.listdir('./logs') if f.endswith('.log')]
    
    return render_template_string(HTML_TEMPLATE, 
                                timestamp=timestamp,
                                scraper_log=scraper_log,
                                log_files=log_files)

@app.route('/download/<filename>')
def download_log(filename):
    """Download log file"""
    try:
        return send_file(f'./logs/{filename}', as_attachment=True)
    except:
        return "File not found", 404

@app.route('/health')
def health():
    """Health check endpoint"""
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080) 