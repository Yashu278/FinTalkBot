# 🤖 FinTalkBot - AI-Powered Financial Chatbot

<div align="center">

![FinTalkBot Logo](https://img.shields.io/badge/FinTalkBot-AI%20Financial%20Chatbot-blue?style=for-the-badge&logo=robot)
![Python](https://img.shields.io/badge/Python-3.11+-green?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-3.1.2-red?style=for-the-badge&logo=flask)
![Docker](https://img.shields.io/badge/Docker-Supported-blue?style=for-the-badge&logo=docker)

*An intelligent financial chatbot that provides real-time stock data, financial news, sentiment analysis, and AI-powered responses*

[🚀 Quick Start](#-quick-start) • [📖 Documentation](#-documentation) • [🔧 Features](#-features) • [📁 Project Structure](#-project-structure) • [🤝 Contributing](#-contributing)

</div>

---

## 📋 Table of Contents

- [🎯 Overview](#-overview)
- [✨ Features](#-features)
- [📁 Project Structure](#-project-structure)
- [🚀 Quick Start](#-quick-start)
- [🔧 Installation](#-installation)
- [⚙️ Configuration](#️-configuration)
- [🎮 Usage](#-usage)
- [🌐 API Reference](#-api-reference)
- [🐳 Docker Deployment](#-docker-deployment)
- [📊 Project Evolution](#-project-evolution)
- [🛠️ Development](#️-development)
- [🔒 Security](#-security)
- [📝 License](#-license)
- [🤝 Contributing](#-contributing)
- [📞 Support](#-support)

---

## 🎯 Overview

FinTalkBot is a comprehensive financial chatbot application that combines traditional rule-based responses with modern AI capabilities. It provides real-time stock market data, financial news analysis, and intelligent conversational responses to help users make informed financial decisions.

### 🎪 Key Highlights

- **🔄 Dual Mode Operation**: Switch between rule-based and AI-powered responses
- **📈 Real-time Data**: Live stock prices, historical data, and market trends
- **📰 News Analysis**: Financial news with sentiment analysis
- **📊 Visual Charts**: Interactive price history charts
- **🤖 Multi-AI Support**: OpenAI GPT and Google Gemini integration
- **🐳 Production Ready**: Docker support for easy deployment
- **💾 Data Persistence**: SQLite database for chat history
- **🔒 Secure**: Environment-based configuration with no exposed secrets

---

## ✨ Features

### 🎯 Core Functionality
- **Stock Price Queries**: Get real-time stock prices for any ticker symbol
- **Company Aliases**: Support for company names (Apple → AAPL, Tesla → TSLA)
- **Price Comparisons**: Compare multiple stocks side by side
- **Historical Data**: 5-day price history with visual charts
- **Financial News**: Latest market news with sentiment analysis
- **Interactive Chat**: Natural language processing for financial queries

### 🤖 AI Integration
- **OpenAI GPT**: Advanced language model integration
- **Google Gemini**: Alternative AI provider support
- **Context Awareness**: Maintains conversation context
- **Smart Responses**: AI-powered financial advice and analysis
- **Fallback System**: Graceful degradation to rule-based responses

### 🛠️ Technical Features
- **RESTful API**: Clean API endpoints for integration
- **Web Interface**: Modern, responsive chat UI
- **Database Logging**: Persistent chat history storage
- **Error Handling**: Robust error management and logging
- **Configuration Management**: Environment-based settings
- **Docker Support**: Containerized deployment
- **Health Monitoring**: Built-in health check endpoints

---

## 📁 Project Structure

```
FinTalkBot/
├── 📁 1st_Draft/                 # Initial prototype
│   ├── src/                      # Source code
│   ├── requirements.txt          # Dependencies
│   └── README.md                 # Basic documentation
├── 📁 2nd_Draft/                 # Enhanced version
│   ├── src/                      # Source code with config
│   ├── Dockerfile               # Container configuration
│   └── requirements.txt          # Updated dependencies
├── 📁 3rd_Draft/                 # Docker integration
│   ├── src/                      # Source code
│   ├── Dockerfile               # Production container
│   └── requirements.txt          # Dependencies
├── 📁 4th_Draft/                 # Database integration
│   ├── src/                      # Source code with storage
│   ├── docker-compose.yml       # Multi-container setup
│   └── requirements.txt          # Dependencies
├── 📁 5th_Draft/                 # 🚀 LATEST VERSION
│   ├── src/                      # Complete source code
│   │   ├── app.py               # Flask application
│   │   ├── chatbot.py           # Chat logic
│   │   ├── data_fetcher.py      # Stock data API
│   │   ├── sentiment_analyzer.py # News sentiment
│   │   ├── ai_client.py         # AI integration
│   │   ├── storage.py           # Database operations
│   │   ├── config.py            # Configuration
│   │   └── templates/           # Web templates
│   ├── docker-compose.yml       # Production setup
│   ├── Dockerfile               # Container config
│   └── requirements.txt          # All dependencies
├── 📄 env.example               # Environment template
├── 📄 .gitignore                # Git ignore rules
├── 📄 README.md                 # This file
└── 📄 PROJECT_DESCRIPTION.md    # Project overview
```

### 🏗️ Architecture Overview

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Web Browser   │    │   Mobile App    │    │   API Client    │
└─────────┬───────┘    └─────────┬───────┘    └─────────┬───────┘
          │                      │                      │
          └──────────────────────┼──────────────────────┘
                                 │
                    ┌─────────────▼─────────────┐
                    │      Flask Web App        │
                    │    (5th_Draft/src/)       │
                    └─────────────┬─────────────┘
                                  │
          ┌───────────────────────┼───────────────────────┐
          │                       │                       │
┌─────────▼─────────┐    ┌────────▼────────┐    ┌────────▼────────┐
│   Rule-based      │    │   AI Client     │    │   Data Fetcher  │
│   Chatbot Logic   │    │  (OpenAI/Gemini)│    │  (yfinance API) │
└─────────┬─────────┘    └────────┬────────┘    └────────┬────────┘
          │                       │                       │
          └───────────────────────┼───────────────────────┘
                                  │
                    ┌─────────────▼─────────────┐
                    │    SQLite Database        │
                    │    (Chat History)         │
                    └───────────────────────────┘
```

---

## 🚀 Quick Start

### ⚡ 30-Second Setup

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/FinTalkBot.git
cd FinTalkBot/5th_Draft

# Install dependencies
pip install -r requirements.txt

# Set up environment (optional - works without API keys)
cp ../env.example .env

# Run the application
python -m src.app
```

**🎉 That's it!** Open `http://localhost:5000` in your browser and start chatting!

---

## 🔧 Installation

### 📋 Prerequisites

- **Python 3.11+** (recommended: Python 3.13)
- **Git** (for cloning)
- **Internet connection** (for stock data and AI features)

### 🐍 Python Installation

#### Windows
```bash
# Using winget
winget install Python.Python.3.13

# Or download from python.org
# https://www.python.org/downloads/
```

#### macOS
```bash
# Using Homebrew
brew install python@3.13

# Or download from python.org
```

#### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install python3.13 python3.13-venv python3.13-pip
```

### 📦 Step-by-Step Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/FinTalkBot.git
   cd FinTalkBot
   ```

2. **Navigate to Latest Version**
   ```bash
   cd 5th_Draft
   ```

3. **Create Virtual Environment**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate
   
   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

4. **Install Dependencies**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

5. **Verify Installation**
   ```bash
   python -c "import flask, yfinance, nltk; print('✅ All dependencies installed successfully!')"
   ```

---

## ⚙️ Configuration

### 🔑 Environment Variables

Create a `.env` file in the `5th_Draft` directory:

```bash
cp ../env.example .env
```

#### 📝 Required Configuration

| Variable | Description | Example | Required |
|----------|-------------|---------|----------|
| `OPENAI_API_KEY` | OpenAI API key for GPT models | `sk-...` | For AI mode |
| `GEMINI_API_KEY` | Google Gemini API key | `AIza...` | For AI mode |

#### ⚙️ Optional Configuration

| Variable | Description | Default | Options |
|----------|-------------|---------|---------|
| `AI_PROVIDER` | AI service provider | `openai` | `openai`, `gemini` |
| `OPENAI_MODEL` | OpenAI model to use | `gpt-4o-mini` | `gpt-4o`, `gpt-4o-mini`, `gpt-3.5-turbo` |
| `GEMINI_MODEL` | Gemini model to use | `gemini-1.5-flash` | `gemini-1.5-flash`, `gemini-1.5-pro` |
| `FLASK_DEBUG` | Enable debug mode | `true` | `true`, `false` |
| `PORT` | Server port | `5000` | Any available port |
| `HOST` | Server host | `0.0.0.0` | `localhost`, `0.0.0.0` |
| `LOG_LEVEL` | Logging level | `INFO` | `DEBUG`, `INFO`, `WARNING`, `ERROR` |
| `SECRET_KEY` | Flask secret key | `dev-secret-change-me` | Random string |

### 🔐 API Key Setup

#### OpenAI API Key
1. Visit [OpenAI Platform](https://platform.openai.com/api-keys)
2. Create a new API key
3. Add to `.env`: `OPENAI_API_KEY=sk-your-key-here`

#### Google Gemini API Key
1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new API key
3. Add to `.env`: `GEMINI_API_KEY=your-key-here`

---

## 🎮 Usage

### 🌐 Web Interface

1. **Start the Application**
   ```bash
   python -m src.app
   ```

2. **Open Browser**
   - Navigate to `http://localhost:5000`
   - You'll see the FinTalkBot chat interface

3. **Chat Examples**
   ```
   User: "What's the price of Apple stock?"
   Bot: "📈 AAPL
        Price: USD $150.25
        Change: ▲ +2.15% today"

   User: "Show me Tesla news"
   Bot: "Here are the latest finance news with sentiment analysis:
        1. Tesla reports record Q4 deliveries
           Sentiment: Positive
        2. Tesla stock surges on new model announcement
           Sentiment: Positive"

   User: "Compare Apple and Microsoft"
   Bot: "🔁 Comparison:
        - AAPL: Price: USD $150.25 | Change: ▲ +2.15% today
        - MSFT: Price: USD $380.50 | Change: ▼ -1.20% today"
   ```

### 🤖 AI Mode

Toggle "AI Mode" in the web interface to enable AI-powered responses:

```
User: "Should I invest in renewable energy stocks?"
AI Bot: "Renewable energy is a growing sector with strong long-term potential. 
         Consider companies like TSLA, ENPH, or ICLN ETF. However, always 
         do your own research and consider your risk tolerance before investing."
```

### 📱 API Usage

#### Send a Message
```bash
curl -X POST http://localhost:5000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "What is the price of AAPL?"}'
```

#### Response
```json
{
  "reply": "📈 AAPL\nPrice: USD $150.25\nChange: ▲ +2.15% today",
  "status": "success",
  "user_input": "What is the price of AAPL?"
}
```

#### AI Mode Request
```bash
curl -X POST http://localhost:5000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Explain market volatility", "mode": "ai"}'
```

---

## 🌐 API Reference

### 📡 Endpoints

#### `GET /`
- **Description**: Serves the main chat interface
- **Response**: HTML page with chat UI

#### `POST /chat`
- **Description**: Send a message to the chatbot
- **Content-Type**: `application/json`
- **Body**:
  ```json
  {
    "message": "Your question here",
    "mode": "ai"  // Optional: "ai" for AI mode, omit for rule-based
  }
  ```
- **Response**:
  ```json
  {
    "reply": "Bot response",
    "status": "success",
    "user_input": "Your original message"
  }
  ```

#### `GET /get?msg=<message>`
- **Description**: Alternative GET endpoint for simple queries
- **Parameters**: `msg` - The message to send
- **Response**: JSON with bot response

#### `GET /health`
- **Description**: Health check endpoint
- **Response**:
  ```json
  {
    "status": "healthy",
    "service": "FinTalkBot API"
  }
  ```

### 🔧 Error Handling

All endpoints return appropriate HTTP status codes:
- `200` - Success
- `400` - Bad Request (missing message)
- `404` - Not Found
- `405` - Method Not Allowed
- `500` - Internal Server Error

---

## 🐳 Docker Deployment

### 🚀 Quick Docker Setup

```bash
cd 5th_Draft

# Set up environment variables
cp ../env.example .env
# Edit .env with your API keys

# Build and run with Docker Compose
docker compose up --build -d
```

### 🔧 Manual Docker Build

```bash
# Build the image
docker build -t fintalkbot:latest .

# Run the container
docker run -d \
  --name fintalkbot \
  -p 5000:5000 \
  -e OPENAI_API_KEY=your-key-here \
  -e GEMINI_API_KEY=your-key-here \
  fintalkbot:latest
```

### 📊 Docker Compose Configuration

The `docker-compose.yml` includes:
- **Web Service**: Flask application
- **Volume Mounting**: Persistent data storage
- **Environment Variables**: Secure configuration
- **Port Mapping**: External access on port 5000

---

## 📊 Project Evolution

### 🏗️ Development Timeline

#### 1st Draft - Foundation
- **Focus**: Basic functionality
- **Features**: Stock price fetching, simple chat interface
- **Tech Stack**: Flask, yfinance, BeautifulSoup
- **Status**: ✅ Complete

#### 2nd Draft - Configuration
- **Focus**: Production readiness
- **Features**: Environment configuration, error handling, logging
- **Tech Stack**: Added config.py, improved error handling
- **Status**: ✅ Complete

#### 3rd Draft - Containerization
- **Focus**: Deployment
- **Features**: Docker support, production server (Gunicorn)
- **Tech Stack**: Dockerfile, Gunicorn
- **Status**: ✅ Complete

#### 4th Draft - Data Persistence
- **Focus**: User experience
- **Features**: Chat history, database storage, Docker Compose
- **Tech Stack**: SQLite, Peewee ORM, docker-compose.yml
- **Status**: ✅ Complete

#### 5th Draft - AI Integration 🚀
- **Focus**: Intelligence
- **Features**: AI-powered responses, multi-provider support
- **Tech Stack**: OpenAI API, Google Gemini, advanced chat logic
- **Status**: ✅ **CURRENT VERSION**

### 🔮 Future Roadmap

- **6th Draft**: Advanced analytics and portfolio management
- **7th Draft**: Real-time notifications and alerts
- **8th Draft**: Mobile app integration
- **9th Draft**: Machine learning predictions
- **10th Draft**: Multi-language support

---

## 🛠️ Development

### 🏃‍♂️ Running in Development Mode

```bash
cd 5th_Draft
export FLASK_DEBUG=true
export LOG_LEVEL=DEBUG
python -m src.app
```

### 🧪 Testing

```bash
# Test basic functionality
python -c "from src.chatbot import chatbot_response; print(chatbot_response('Hello'))"

# Test API endpoints
curl http://localhost:5000/health

# Test with sample data
python -c "from src.data_fetcher import get_stock_price; print(get_stock_price('AAPL'))"
```

### 🔍 Debugging

Enable debug mode for detailed logging:
```bash
export FLASK_DEBUG=true
export LOG_LEVEL=DEBUG
python -m src.app
```

### 📝 Code Structure

```
src/
├── app.py                 # Flask application and routes
├── chatbot.py            # Core chat logic and responses
├── data_fetcher.py       # Stock data and news fetching
├── sentiment_analyzer.py # News sentiment analysis
├── ai_client.py          # AI provider integration
├── storage.py            # Database operations
├── config.py             # Configuration management
└── templates/
    └── index.html        # Web interface template
```

### 🎯 Key Functions

- `chatbot_response()` - Main chat logic
- `get_stock_price()` - Fetch stock data
- `analyze_sentiment()` - News sentiment analysis
- `generate_ai_reply()` - AI-powered responses
- `log_chat()` - Store chat history

---

## 🔒 Security

### 🛡️ Security Measures

1. **API Key Protection**
   - All API keys stored in environment variables
   - No hardcoded secrets in source code
   - `.env` files excluded from version control

2. **Input Validation**
   - Sanitized user inputs
   - SQL injection prevention
   - XSS protection in templates

3. **Error Handling**
   - Graceful error responses
   - No sensitive information in error messages
   - Comprehensive logging

4. **Dependencies**
   - Regular dependency updates
   - Security vulnerability scanning
   - Minimal dependency footprint

### 🔐 Best Practices

- **Never commit API keys** to version control
- **Use environment variables** for all sensitive data
- **Regular security updates** for dependencies
- **Monitor API usage** to prevent abuse
- **Implement rate limiting** for production use

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### 📄 License Summary

- ✅ Commercial use allowed
- ✅ Modification allowed
- ✅ Distribution allowed
- ✅ Private use allowed
- ❌ No liability or warranty

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### 🚀 Quick Contribution Guide

1. **Fork the Repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/FinTalkBot.git
   cd FinTalkBot
   ```

2. **Create a Feature Branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```

3. **Make Your Changes**
   - Follow the existing code style
   - Add tests for new features
   - Update documentation

4. **Test Your Changes**
   ```bash
   cd 5th_Draft
   python -m src.app
   # Test your changes thoroughly
   ```

5. **Commit and Push**
   ```bash
   git commit -m "Add amazing feature"
   git push origin feature/amazing-feature
   ```

6. **Create a Pull Request**
   - Describe your changes clearly
   - Reference any related issues
   - Wait for review and feedback

### 🎯 Contribution Areas

- **🐛 Bug Fixes**: Report and fix issues
- **✨ New Features**: Add functionality
- **📚 Documentation**: Improve guides and examples
- **🧪 Testing**: Add test coverage
- **🎨 UI/UX**: Improve the web interface
- **🔧 DevOps**: Enhance deployment and CI/CD

### 📋 Development Guidelines

- **Code Style**: Follow PEP 8 for Python
- **Documentation**: Update README for new features
- **Testing**: Test all changes thoroughly
- **Security**: Never commit sensitive data
- **Performance**: Consider optimization for new features

---

## 📞 Support

### 🆘 Getting Help

- **📖 Documentation**: Check this README first
- **🐛 Bug Reports**: Open an issue on GitHub
- **💡 Feature Requests**: Submit a feature request
- **💬 Discussions**: Use GitHub Discussions for questions

### 🔗 Useful Links

- **GitHub Repository**: [FinTalkBot](https://github.com/YOUR_USERNAME/FinTalkBot)
- **Issue Tracker**: [Report Issues](https://github.com/YOUR_USERNAME/FinTalkBot/issues)
- **Discussions**: [Community Forum](https://github.com/YOUR_USERNAME/FinTalkBot/discussions)

### 📧 Contact

- **GitHub**: [@YOUR_USERNAME](https://github.com/Yashu278/FinTalkBot)
- **Email**: your-email@example.com
- **LinkedIn**: [Your Profile](https://www.linkedin.com/in/yashdeep-saxena-3a6914295/)

---

<div align="center">

### 🌟 Star this repository if you found it helpful!

**Made with ❤️ by [Your Name](https://github.com/Yashu278)**

[⬆ Back to Top](#-fintalkbot---ai-powered-financial-chatbot)

</div>

