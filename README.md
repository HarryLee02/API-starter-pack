# API Starter Pack - Zendesk Documentation Processor

A comprehensive tool for processing and analyzing Zendesk help center documentation using OpenAI's API. The main purpose of this project is to demonstrate how to work with APIs, preprocess data, and deploy AI-powered documentation analysis with Docker containerization and reverse proxy setup.

## Demo

🌐 **Live Demo**: https://logs.harrylee.id.vn/

## 🚀 Overview

This project provides an automated solution for:
- Scraping Zendesk help center articles and categories
- Processing and organizing documentation into structured formats
- Analyzing token usage and content distribution
- Preparing data for AI-powered assistants and vector stores
- **Docker containerization** with reverse proxy for production deployment

## ✨ Features

- **Automated Documentation Scraping**: Fetches articles and categories from Zendesk help center
- **Content Organization**: Organizes articles by category in a structured file system
- **Token Analysis**: Analyzes and visualizes token distribution across documentation
- **OpenAI Integration**: Uploads processed files to vector store for AI assistant training
- **Progress Tracking**: Detailed logging and progress monitoring with web interface
- **Error Handling**: Robust error handling for API failures and file operations
- **Docker Support**: Complete containerization with multi-service architecture
- **Reverse Proxy**: Caddy-based reverse proxy for domain routing and SSL termination

## 🛠️ Setup

### Prerequisites

- **For Local Development**:
  - Python 3.7+
  - Zendesk API access
  - OpenAI API key
  - Required Python packages (see installation below)

- **For Docker Deployment**:
  - Docker and Docker Compose
  - Domain name (optional, for production)
  - Zendesk API access
  - OpenAI API key

### Installation

#### Option 1: Docker Deployment (Recommended)

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd API-starter-pack
   ```

2. **Environment Configuration**

   Create a `.env` file in the root directory based on `env.sample`:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   OPENAI_VECTOR_STORE_ID=your_vector_store_id
   SUPPORT_URL=https://your-zendesk-instance.zendesk.com/api/v2/help_center
   ```

3. **Configure Domain (Optional)**

   Edit the `Caddyfile` to use your domain:
   ```nginx
   your-domain.com {
       reverse_proxy log-server:8080 {
         flush_interval -1
       }
   }
   ```
#### Option 2: Local Python Development

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd API-starter-pack
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

   Required dependencies:
   - OpenAI
   - requests
   - Markdown
   - python-dotenv

3. **Environment Configuration**

   Create a `.env` file in the root directory:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   OPENAI_VECTOR_STORE_ID=your_vector_store_id
   SUPPORT_URL=https://your-zendesk-instance.zendesk.com/api/v2/help_center
   ```

## 🏃 How to Run

### Docker Deployment

```bash
# Start all services
docker-compose up -d --build

# Stop services
docker-compose down
```

This will start:
- **Scraper Service**: Processes Zendesk documentation
- **Log Server**: Web interface for monitoring (port 8080)
- **Caddy**: Reverse proxy with automatic SSL (ports 80/443)

Access via:
- **Local**: http://localhost
- **With Domain**: https://your-domain.com

### Local Python Development

```bash
# Run scraper
python main.py

# Run log server on localhost:8080
python log-server/app.py
```

This setup will only run on localhost without domain

## Analyze Token Usage
For better chunking strategy while attaching files to vector store, I make a script to count all the files tokens and make decision.
```bash
python src/count_tokens.py
```

This will:
- Count tokens in all markdown files
- Generate statistical analysis
- Create visualizations of token distribution
- Display file count by token ranges

## 🐳 Docker Architecture

The project uses a multi-service Docker architecture:

```
┌─────────────────┐     ┌─────────────────┐       ┌─────────────────┐
│   Caddy Proxy   │     │   Log Server    │       │     Scraper     │
│  (Port 80/443)  │────>│   (Port 8080)   │◄──────│   (Background)  │
└─────────────────┘     └─────────────────┘       └─────────────────┘
         │                       │                       │
         │                       │                       │
         ▼                       ▼                       ▼
   ┌────────────────────────────────────────────────────────────────┐
   │                       Shared Volumes                           │
   │     ┌──────────────┐  ┌─────────────┐  ┌──────────────┐        │
   │     │ scraper-logs │  │ docs-volume │  │  caddy_data  │        │
   │     └──────────────┘  └─────────────┘  └──────────────┘        │
   └────────────────────────────────────────────────────────────────┘
```

### Services

- **scraper**: Main application that processes Zendesk documentation
- **log-server**: Flask web server providing monitoring interface
- **caddy**: Reverse proxy with automatic SSL certificate management

### Volumes

- **scraper-logs**: Shared logs between scraper and log server
- **docs-volume**: Processed documentation files
- **caddy_data**: SSL certificates and Caddy data
- **caddy_config**: Caddy configuration

## 📊 Project Structure

```
API-starter-pack/
├── docker-compose.yml      # Docker services configuration
├── Dockerfile              # Main application container
├── Caddyfile              # Reverse proxy configuration
├── main.py                # Main scraping script
├── src/
│   ├── count_tokens.py    # Token analysis tool
│   ├── delete_files.py    # File cleanup utility
│   └── upload.py          # OpenAI upload utility
├── log-server/
│   ├── app.py             # Flask web server
│   ├── Dockerfile         # Log server container
│   ├── requirements.txt   # Log server dependencies
│   └── templates/
│       └── index.html     # Web interface
├── docs/                  # Processed documentation
│   ├── category-1/
│   │   ├── articles.json
│   │   └── article-files.md
│   └── category-2/
├── static/                # Static assets and screenshots
├── .env                   # Environment variables
└── README.md             # This file
```

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `OPENAI_API_KEY` | Your OpenAI API key | Yes |
| `OPENAI_VECTOR_STORE_ID` | OpenAI vector store ID | Yes |
| `SUPPORT_URL` | Zendesk help center API URL | Yes |

### Caddy Configuration

The `Caddyfile` configures the reverse proxy:

```nginx
# Eg. logs.harrylee.id.vn
<your-domain> {
    reverse_proxy log-server:8080 {
      flush_interval -1
    }
}
```

Features:
- Automatic SSL certificate generation
- Domain-based routing

### API Endpoints Used

- `GET /api/v2/help_center/categories/` - Fetch all categories
- `GET /api/v2/help_center/categories/{id}/articles` - Fetch articles by category

## 📈 Timeline
It took me 1 week in total to code, debug, deploy and write reports. The phases below are not necessarily in order, just an estimate of the total time since I spent most of my time writing documents.

### Phase 1: Initial Setup & Research
**Duration**: ~1 hours
- Repository creation and initial setup
- Zendesk API, OpenAI, and Digital Ocean research
- Basic project structure implementation

### Phase 2: Scraper Development
**Duration**: ~2 hours
- Scrape files from Zendesk API 
- Convert and process data to make clean Markdown file
- Storing files for display
- Error handling (add, update, skip), optimization and docker containerization

### Phase 3: OpenAI Assistant Development & Files Processing
**Duration**: ~4 hours
- Token analysis implementation to decise chunking strategy
- Uploading files and attach to vector store via OpenAI API
- Error handling, optimization and docker containerization

### Phase 4: Scraper Cronjob
**Duration**: ~1 hour
- Setup Linux cronjob
- Caddy reverse proxy integration
- Production deployment configuration

### Phase 5: Documentation
**Duration**: ~5 hours

- Writing reports and README.md

## 🤝 Contributing
This is meant to be a 1-time task but if the submitted features look feasible to me, I will consider.
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Bottom Text**: This project is designed for educational and practical purposes. Please ensure you have proper authorization to access and process the Zendesk data you're working with.