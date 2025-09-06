# Notion RAG Agent

A Retrieval-Augmented Generation (RAG) agent that queries a Notion knowledge base to provide intelligent responses using AI models.

## 🚀 Features

- **Notion Integration**: Connects directly to your Notion database as a knowledge source
- **Multi-Model Support**: Compatible with both OpenAI and Gemini AI models
- **Intelligent Retrieval**: Semantic search across Q&A pairs in your Notion database
- **Configurable Knowledge Base**: Easy setup with your existing Notion database
- **Environment-Based Configuration**: Secure management of API keys and settings

## 📋 Prerequisites

- Python 3.8+
- Notion account with a database containing Q&A content
- OpenAI API key and/or Google Gemini API key

## ⚙️ Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd notion-rag-agent
```
2. Install dependencies:

pip install -r requirements.txt

3. Set up environment variables in .env file:

NOTION_TOKEN=your_notion_integration_token
api_key_openai=your_openai_api_key
id_openai=your_openai_model_id

## 🏗️ Architecture

The system consists of:

- **Notion Client**: Handles connection and queries to your Notion database
- **Knowledge Retriever**: Searches and retrieves relevant Q&A pairs  
- **AI Agent**: Processes queries and generates responses using retrieved context
- **Model Providers**: Supports multiple AI models (OpenAI, Gemini)

## 🎯 Usage

Run the agent:
```bash
python main.py

```

Enter your query when prompted, and the agent will:

1. Search your Notion knowledge base for relevant Q&A pairs
2. Use the AI model to generate a context-aware response
3. Display the response with source information

## 🔧 Configuration

### Notion Database Setup

Your Notion database should contain these properties:

- `Questions1` (title property)
- `Answer1` (rich_text property) 
- `Question2` (rich_text property, optional)
- `Answer2` (rich_text property, optional)

## 📊 Knowledge Retrieval

The system uses a keyword matching algorithm to:

- Split queries into keywords
- Search through all Q&A pairs in Notion
- Score matches based on keyword frequency
- Return the most relevant documents

## 🛠️ Dependencies

- `agno` - Agent framework
- `notion_client` - Notion API integration
- `python-dotenv` - Environment variable management
- `openai` - OpenAI API client
- `google-generativeai` - Gemini API client

## 🔮 Future Enhancements

- Vector-based semantic search
- Support for additional AI models
- Web interface
- Batch processing capabilities
- Advanced filtering options

## 📝 License

MIT License - see LICENSE file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.