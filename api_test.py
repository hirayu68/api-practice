# 環境変数を読み込む
from dotenv import load_dotenv
import os, requests

# 取得したいAPIのURL
# 環境変数を読み込む
load_dotenv()
api_key = os.getenv("OPENWEATHER_API_KEY")

# 定数
CITY = "Tokyo"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={api_key}&units=metric&lang=ja"


response = requests.get(URL)
data = response.json()

# data情報を天気、気温、湿度、風速を表示
print(f"天気: {data['weather'][0]['description']}")
print(f"気温: {data['main']['temp']}°C")
print(f"湿度: {data['main']['humidity']}%")
print(f"風速: {data['wind']['speed']} m/s")
