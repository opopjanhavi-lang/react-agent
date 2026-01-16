from langchain_core.tools import tool
from dotenv import load_dotenv
from tavily import TavilyClient
import os
import requests
from datetime import datetime, timedelta
load_dotenv()
tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

@tool
def web_search(query: str) -> str:
    """
    Searches the web for recent and relevant information and returns summarized results.
    """
    response = tavily.search(
        query=query,
        search_depth="advanced",
        max_results=3
    )

    results = []
    for item in response.get("results", []):
        results.append(f"Title: {item['title']}\nSnippet: {item['content']}")

    return "\n\n".join(results)
@tool
def weather(location_and_day: str) -> str:
    """
    Fetches current or future weather using OpenWeather API.

    Input examples:
    - "Mumbai today"
    - "Boisar after 2 days"
    - "What is the weather in Delhi today?"
    """

    api_key = os.getenv("OPENWEATHER_API_KEY")

    text = location_and_day.lower()

    if "after" in text:
        city = text.split("after")[0]
    elif "today" in text:
        city = text.split("today")[0]
    else:
        city = text

    city = (
        city.replace("what is the weather in", "")
        .replace("weather in", "")
        .replace("in", "")
        .strip()
        .title()
    )

    # CURRENT WEATHER
    if "after" not in text:
        url = (
            f"https://api.openweathermap.org/data/2.5/weather"
            f"?q={city},IN&appid={api_key}&units=metric"
        )

        response = requests.get(url).json()

        if response.get("cod") != 200:
            return f"Sorry, I could not fetch weather data for {city}."

        return (
            f"Current weather in {city}: "
            f"{response['main']['temp']}°C, "
            f"{response['weather'][0]['description']}"
        )

    # FUTURE WEATHER
    url = (
        f"https://api.openweathermap.org/data/2.5/forecast"
        f"?q={city},IN&appid={api_key}&units=metric"
    )

    response = requests.get(url).json()

    if "list" not in response:
        return f"Sorry, forecast data not available for {city}."

    days = int(text.split("after")[1].split()[0])
    target_date = (datetime.now() + timedelta(days=days)).date()

    for item in response["list"]:
        if datetime.fromtimestamp(item["dt"]).date() == target_date:
            return (
                f"Predicted weather in {city} after {days} days: "
                f"{item['main']['temp']}°C, "
                f"{item['weather'][0]['description']}"
            )

    return f"Weather forecast for {city} after {days} days is not available."
