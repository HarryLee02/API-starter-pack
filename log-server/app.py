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
        <h2>Latest Scraper Log <span id="status-indicator" style="color: #28a745;">●</span></h2>
        <a href="/download/scraper.log" class="download-link">Download Log File</a>
        <button onclick="toggleAutoRefresh()" id="refresh-btn" style="padding: 5px 10px; background: #007bff; color: white; border: none; border-radius: 3px; cursor: pointer; margin-left: 10px;">Auto Refresh: ON</button>
        <div class="log-content" id="log-content">{{ scraper_log }}</div>
    </div>
    
    <div class="log-section">
        <h2>Available Log Files</h2>
        <ul>
        {% for log_file in log_files %}
            <li><a href="/download/{{ log_file }}">{{ log_file }}</a></li>
        {% endfor %}
        </ul>
    </div>
    
    <script>
    let autoRefreshInterval;
    let isAutoRefreshOn = true;
    
    // Start auto-refresh on page load
    startAutoRefresh();
    
    function startAutoRefresh() {
        autoRefreshInterval = setInterval(updateLogs, 2000); // Update every 2 seconds
    }
    
    function stopAutoRefresh() {
        clearInterval(autoRefreshInterval);
    }
    
    function toggleAutoRefresh() {
        const btn = document.getElementById('refresh-btn');
        if (isAutoRefreshOn) {
            stopAutoRefresh();
            btn.textContent = 'Auto Refresh: OFF';
            btn.style.background = '#dc3545';
            document.getElementById('status-indicator').style.color = '#dc3545';
        } else {
            startAutoRefresh();
            btn.textContent = 'Auto Refresh: ON';
            btn.style.background = '#007bff';
            document.getElementById('status-indicator').style.color = '#28a745';
        }
        isAutoRefreshOn = !isAutoRefreshOn;
    }
    
    function updateLogs() {
        fetch('/api/logs')
            .then(response => response.json())
            .then(data => {
                if (data.status === 'success') {
                    const logContent = document.getElementById('log-content');
                    if (logContent.textContent !== data.logs) {
                        logContent.textContent = data.logs;
                        logContent.scrollTop = logContent.scrollHeight; // Auto-scroll to bottom
                    }
                }
            })
            .catch(error => {
                console.error('Error updating logs:', error);
            });
    }
    </script>
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

@app.route('/api/logs')
def get_logs():
    """API endpoint to get latest logs"""
    try:
        if os.path.exists('./logs/scraper.log'):
            with open('./logs/scraper.log', 'r') as f:
                log_content = f.read()
            return {"status": "success", "logs": log_content}
        else:
            return {"status": "error", "message": "No log file found"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

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