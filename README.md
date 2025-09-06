# FinTalkBot - AI-Powered Financial Chatbot

FinTalkBot is an intelligent financial chatbot that provides real-time stock prices, financial news, sentiment analysis, and AI-powered responses. The project includes multiple draft versions showing the evolution of the application.

## 🚀 Features

- **Real-time Stock Data**: Get current stock prices and historical data
- **Financial News**: Latest financial news with sentiment analysis
- **AI Integration**: Support for both OpenAI GPT and Google Gemini
- **Interactive Charts**: Visual representation of stock price history
- **Dual Mode**: Switch between rule-based responses and AI-powered responses
- **Docker Support**: Easy deployment with Docker and Docker Compose
- **Database Logging**: Chat history stored in SQLite database

## 📁 Project Structure

- `1st_Draft/` - Initial version with basic functionality
- `2nd_Draft/` - Enhanced with configuration management
- `3rd_Draft/` - Added Docker support
- `4th_Draft/` - Added database storage
- `5th_Draft/` - **Latest version** with AI integration

## 🛠️ Quick Start (5th Draft - Recommended)

### Prerequisites
- Python 3.11+
- Git

### Setup

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd FinTalkBot
   ```

2. **Navigate to the latest version**
   ```bash
   cd 5th_Draft
   ```

3. **Create virtual environment**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up environment variables**
   ```bash
   cp ../env.example .env
   # Edit .env file with your actual API keys
   ```

6. **Run the application**
   ```bash
   python -m src.app
   ```

7. **Access the application**
   - Open your browser and go to `http://localhost:5000`

### Docker Setup

```bash
cd 5th_Draft
cp ../env.example .env
# Edit .env file with your actual API keys
docker compose up --build -d
```

## 🔑 Environment Variables

Copy `env.example` to `.env` and configure the following variables:

### Required for AI Features
- `OPENAI_API_KEY` - Your OpenAI API key (for GPT models)
- `GEMINI_API_KEY` - Your Google Gemini API key (alternative to OpenAI)

### Optional Configuration
- `AI_PROVIDER` - Choose between "openai" or "gemini"
- `OPENAI_MODEL` - OpenAI model (default: gpt-4o-mini)
- `GEMINI_MODEL` - Gemini model (default: gemini-1.5-flash)
- `FLASK_DEBUG` - Enable debug mode (default: true)
- `PORT` - Port number (default: 5000)

## 🎯 Usage

### Web Interface
- Visit `http://localhost:5000` for the interactive chat interface
- Toggle "AI Mode" to switch between rule-based and AI responses
- Ask questions like:
  - "What's the price of AAPL?"
  - "Show me Tesla news"
  - "Compare Apple and Microsoft"

### API Endpoints
- `GET /` - Chat interface
- `POST /chat` - Send messages (JSON: `{"message": "your question"}`)
- `GET /health` - Health check

## 🔧 Development

### Project Evolution
Each draft folder represents a different version:
- **1st Draft**: Basic Flask app with stock data fetching
- **2nd Draft**: Added configuration management and error handling
- **3rd Draft**: Docker support and production deployment
- **4th Draft**: Database integration for chat logging
- **5th Draft**: AI integration with multiple providers

### Contributing
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Support

If you encounter any issues or have questions, please open an issue on GitHub.

---

**Note**: Make sure to keep your API keys secure and never commit them to version control. Use the provided `.env` file for local development.
