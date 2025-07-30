# API Starter Pack - Zendesk Documentation Processor

A comprehensive tool for processing and analyzing Zendesk help center documentation using OpenAI's API. This project demonstrates how to work with APIs, preprocess data, and deploy AI-powered documentation analysis.

## Demo

http://174.138.30.161:8080/

## 🚀 Overview

This project provides an automated solution for:
- Scraping Zendesk help center articles and categories
- Processing and organizing documentation into structured formats
- Analyzing token usage and content distribution
- Preparing data for AI-powered assistants and vector stores

## ✨ Features

- **Automated Documentation Scraping**: Fetches articles and categories from Zendesk help center
- **Content Organization**: Organizes articles by category in a structured file system
- **Token Analysis**: Analyzes and visualizes token distribution across documentation
- **OpenAI Integration**: Uploads processed files to OpenAI for AI assistant training
- **Progress Tracking**: Detailed logging and progress monitoring
- **Error Handling**: Robust error handling for API failures and file operations

## 🛠️ Setup

### Prerequisites

- Python 3.7+
- Zendesk API access
- OpenAI API key
- Required Python packages (see installation below)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd API-starter-pack
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
Required dependencies are:
- OpenAI
- requests
- Markdown
- python-dotenv

3. **Environment Configuration**
   Create a `.env` file in the root directory base on `env.example`:
   ```env
   OPENAI_API_KEY = your_openai_api_key_here

   OPENAI_VECTOR_STORE_ID = your_vector_store_id

   SUPPORT_URL = https://your-zendesk-instance.zendesk.com/api/v2/help_center
   ```

## 🏃How to Run Locally
There are 2 options to run this project: `python` or `Docker`
### Python
#### 1. Scrape Documentation
```bash
# run scraper
python main.py

# run log server on localhost:8080
python log-server/app.py
```

This will:
- Fetch all categories from your Zendesk help center via API
- Download articles for each category
- Convert articles to markdown format
- Upload files to OpenAI for processing
- Log everything and display on localhost

#### 2. Analyze Token Usage
```bash
python count_tokens.py
```
This will:
- Count tokens in all markdown files
- Generate statistical analysis
- Create visualizations of token distribution
- Display file count by token ranges

## 📊 Project Structure

```
API-starter-pack/
├── scraper.py              # Main scraping script
├── count_tokens.py         # Token analysis tool
├── docs/                   # Processed documentation
│   ├── category-1/
│   │   ├── articles.json
│   │   └── article-files.md
│   └── category-2/
├── static/                 # Static assets and screenshots
├── .env                    # Environment variables
└── README.md              # This file
```

## 📈 Daily Job Logs

### Phase 1: Initial Setup & Research
**Duration**: ~2 hours
- Repository creation and initial setup
- Zendesk API, OpenAI, and OptiSigns research
- Basic project structure implementation

### Phase 2: Core Development
**Duration**: ~2 hours
- OpenAI API integration challenges and resolution
- File upload and vector store implementation
- Error handling and optimization

### Phase 3: Analysis & Documentation
**Duration**: ~2 hours
- Token analysis implementation
- Documentation and README updates
- Project finalization

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `OPENAI_API_KEY` | Your OpenAI API key | Yes |
| `SUPPORT_URL` | Zendesk help center API URL | Yes |

### API Endpoints Used

- `GET /api/v2/help_center/categories/` - Fetch all categories
- `GET /api/v2/help_center/categories/{id}/articles` - Fetch articles by category

## 📝 Example Usage

### Basic Scraping
```python
# The scraper will automatically:
# 1. Load categories from Zendesk
# 2. Create directory structure
# 3. Download and process articles
# 4. Upload to OpenAI
```

### Token Analysis
```python
# Generate comprehensive token analysis:
# - Statistical summary
# - Distribution visualization
# - File categorization by token count
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

For support and questions:
- Check the [Issues](../../issues) page
- Review the documentation in the `docs/` folder
- Contact the maintainers

## 🔮 Future Enhancements

- [ ] Add support for multiple Zendesk instances
- [ ] Implement incremental updates
- [ ] Add content quality analysis
- [ ] Support for other documentation platforms
- [ ] Enhanced visualization and reporting

---

**Note**: This project is designed for educational and practical purposes. Please ensure you have proper authorization to access and process the Zendesk data you're working with.