import requests
from datetime import datetime
from common.functions import k_to_celsius, ms_to_kmh
from common.config import  AppConfig


API_KEY = AppConfig.API_KEY
CITY = AppConfig.CITY

def get_weather():
    url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()

    weather = {
        "place": data.get("name"),
        "temp": k_to_celsius(data.get("main").get("temp")) ,
        "feels_like": k_to_celsius(data.get("main").get("feels_like")),
        "wind": ms_to_kmh(data.get("wind").get("speed")),
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "sunrise": datetime.fromtimestamp(data.get("sys").get("sunrise")).strftime("%H:%M:%S"),
    }

    return weather

