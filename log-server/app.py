from flask import Flask, render_template, send_file
import os
from datetime import datetime
import markdown

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__, template_folder=os.path.join(BASE_DIR, 'templates'), static_folder=os.path.join(BASE_DIR, 'static'), static_url_path='')

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
    
    return render_template('index.html', 
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

@app.route('/docs')
def docs():
    """List all scraped documents by category"""
    try:
        if os.path.exists('./docs'):
            categories = {}
            for root, dirs, files in os.walk('./docs'):
                # Get category name (folder name)
                category = os.path.basename(root)
                if category != 'docs':  # Skip root docs folder
                    if category not in categories:
                        categories[category] = []
                    
                    # Add only markdown files in this category (exclude JSON files)
                    for file in files:
                        if file.endswith('.md') and not file.endswith('.json'):
                            categories[category].append(file)
            
            return {"status": "success", "categories": categories}
        else:
            return {"status": "error", "message": "No docs directory found"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.route('/docs/<category>')
def get_category(category):
    """Get all documents in a specific category"""
    try:
        category_path = os.path.join('./docs', category)
        if os.path.exists(category_path) and os.path.isdir(category_path):
            files = []
            for file in os.listdir(category_path):
                if file.endswith('.md') and not file.endswith('.json'):
                    files.append(file)
            return {"status": "success", "category": category, "files": files}
        else:
            return {"status": "error", "message": f"Category '{category}' not found"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.route('/docs/<category>/<filename>')
def get_doc(category, filename):
    """Get a specific document from a category"""
    try:
        doc_path = os.path.join('./docs', category, filename)
        if os.path.exists(doc_path) and filename.endswith('.md') and not filename.endswith('.json'):
            with open(doc_path, 'r', encoding='utf-8') as f:
                markdown_content = f.read()
            
            # Convert markdown to HTML
            html_content = markdown.markdown(markdown_content, extensions=['tables', 'fenced_code', 'codehilite'])
            
            return {
                "status": "success", 
                "content": html_content, 
                "raw_content": markdown_content,
                "category": category, 
                "filename": filename
            }
        else:
            return {"status": "error", "message": "Document not found"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080) 