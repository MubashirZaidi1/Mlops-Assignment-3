import requests, os, pandas as pd
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
API_KEY = os.getenv("API_KEY")
CITY = "London"
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

def fetch_weather():
    response = requests.get(URL).json()
    data = {
        "datetime": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "temperature": response["main"]["temp"],
        "humidity": response["main"]["humidity"],
        "wind_speed": response["wind"]["speed"],
        "weather_condition": response["weather"][0]["description"]
    }
    df = pd.DataFrame([data])
    os.makedirs("data", exist_ok=True)
    df.to_csv("data/raw_data.csv", mode='a', header=not os.path.exists("data/raw_data.csv"), index=False)

if __name__ == "__main__":
    fetch_weather()
