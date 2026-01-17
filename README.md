# ReAct Weather Agent 🌦️🤖

A simple **ReAct-style AI Agent** built using **LangChain**, **Groq
LLM**, **Tavily Search**, and the **OpenWeather API**.

This agent can: - Answer general questions - Search the web when
needed - Fetch **current and future weather** for Indian cities using a
real API

------------------------------------------------------------------------

## 🚀 Features

-   ReAct Agent (Reason + Act)
-   Groq-powered LLM (fast inference)
-   Tavily web search tool
-   OpenWeather API integration
-   Natural language weather queries:
    -   *"What is the weather in Mumbai today?"*


------------------------------------------------------------------------

## 📁 Project Structure

    react_agent/
    │
    ├── app/
    │   ├── agent.py        # Agent creation logic
    │   ├── tools.py        # Web search & weather tools
    │   ├── prompts.py     # ReAct prompt template
    │   └── config.py      # LLM & environment config
    │
    ├── main.py             # Entry point
    ├── .env                # API keys
    ├── requirements.txt
    └── README.md

------------------------------------------------------------------------

## 🔑 Environment Variables

Create a `.env` file in the root directory:

    GROQ_API_KEY=your_groq_api_key
    OPENWEATHER_API_KEY=your_openweather_api_key
    TAVILY_API_KEY=your_tavily_api_key

------------------------------------------------------------------------

## 📦 Installation

Create and activate a virtual environment:

``` bash
python -m venv venv
venv\Scripts\activate   # Windows
```

Install dependencies:

``` bash
pip install langchain langchain-core langchain-groq tavily-python python-dotenv requests
```

------------------------------------------------------------------------

## ▶️ Run the Agent

``` bash
python main.py
```

You will see:

    ReAct Agent Ready (type 'exit' to quit)
    User:

------------------------------------------------------------------------

## 🧠 Example Queries

    What is the weather in Mumbai today?
    Boisar after 2 days
    What is today's date?
    Latest AI news in India

------------------------------------------------------------------------

## 🛠️ Weather Tool Logic

-   Uses **OpenWeather current weather API** for "today"
-   Uses **5-day forecast API** for future dates
-   Automatically extracts city names from sentences

------------------------------------------------------------------------

------------------------------------------------------------------------

## 🛠️ Detailed Report

-   The detailed report of the capstone project is present in the file **react_agent.pdf**.

------------------------------------------------------------------------

## ✅ Expected Output

    Current weather in Mumbai: 30.2°C, haze

------------------------------------------------------------------------

## ❗ Notes

-   State-level queries like *"Maharashtra"* are not supported directly
-   Use city names (Mumbai, Pune, Nagpur, etc.)
-   Agent stops automatically if a tool fails repeatedly

------------------------------------------------------------------------

## 📌 Future Improvements

-   State-level weather aggregation
-   Caching API responses
-   UI frontend
-   LangGraph-based agent flow

------------------------------------------------------------------------

## 👨‍💻 Built With

-   LangChain
-   Groq LLM
-   Tavily Search API
-   OpenWeather API
-   Python

------------------------------------------------------------------------

Happy hacking! 🚀
