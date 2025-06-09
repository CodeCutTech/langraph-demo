# Investment Committee Multi-Agent System

A multi-agent system built with LangGraph that simulates an investment committee debate between bullish and bearish perspectives, with a chairman making final investment decisions.

## 🎯 Overview

This system demonstrates true agentic behavior where three AI agents debate and make investment decisions:

- **🐂 Bull Agent**: Finds positive reasons to buy stocks
- **🐻 Bear Agent**: Finds negative reasons to avoid stocks
- **🎯 Chairman Agent**: Makes final investment decisions after hearing both sides

## 🚀 Features

- **Real-time web research** using Tavily search
- **Agentic debate** where agents counter each other's arguments
- **Multi-round discussion** with structured workflow
- **Final decision making** with reasoning
- **Interactive command-line interface**

## 📁 Project Structure

```
investment-committee/
├── src/
│   ├── __init__.py          # Package marker
│   ├── config.py            # Prompts and model configuration
│   ├── tools.py             # Agent tools organized by function
│   ├── utils.py             # Utility functions for display
│   └── agents.py            # Agent and supervisor creation
├── main.py                  # Command-line interface
├── requirements.txt         # Python dependencies
├── .env.example             # Environment variables template
└── README.md                # This file
```

## 🛠️ Installation

1. **Clone and navigate to the directory**

   ```bash
   cd investment-committee
   ```

2. **Install dependencies**

   Install dependencies using [uv](https://github.com/astral-sh/uv), a fast Python package installer and resolver:

   ```bash
   uv sync
   ```

3. **Set up environment variables**

   Next, create an `.env` file and populate it with your API keys from [OpenAI](https://platform.openai.com/) and [Tavily](https://www.tavily.com/).

   ```bash
   cp .env.example .env
   # Edit .env with your API keys
   ```

4. **Run the application**

   Run the application with the `python` command:

   ```bash
   python main.py
   ```

   or with uv:

   ```bash
   uv run main.py
   ```

## 💡 Usage

1. Start the application with `python main.py`
2. Enter any stock symbol (e.g., NVDA, TSLA, AAPL)
3. Watch the agents debate the investment merits
4. See the chairman's final decision with reasoning
5. Type 'quit' to exit

## 🔧 Configuration

- **Model settings**: Modify `src/config.py`
- **Agent prompts**: Customize prompts in `src/config.py`
- **Tool behavior**: Adjust tools in `src/tools.py`

## 📋 Requirements

- Python 3.8+
- OpenAI API key
- Tavily API key (for web search)

## 🎓 Educational Purpose

This project demonstrates:

- Multi-agent system architecture with LangGraph
- Agent-to-agent communication and debate
- Real-time web search integration
- Structured decision-making workflows
- Command-line interface design

Perfect for learning how to build collaborative AI systems!
