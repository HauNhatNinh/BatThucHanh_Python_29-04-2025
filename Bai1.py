import requests
import pandas as pd
from datetime import datetime

# Gọi API
url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 52.52,
    "longitude": 13.41,
    "past_days": 10,
    "hourly": "temperature_2m,relative_humidity_2m,wind_speed_10m"
}
response = requests.get(url, params=params)
data = response.json()

# Trích xuất dữ liệu
df = pd.DataFrame({
    "time": data["hourly"]["time"],
    "temperature_2m": data["hourly"]["temperature_2m"],
    "relative_humidity_2m": data["hourly"]["relative_humidity_2m"],
    "wind_speed_10m": data["hourly"]["wind_speed_10m"]
})

df["latitude"] = data["latitude"]
df["longitude"] = data["longitude"]

# Lưu ra CSV
df.to_csv("weather_data.csv", index=False)

# Lọc dữ liệu tới ngày 29-04
df["time"] = pd.to_datetime(df["time"])
df_filtered = df[df["time"] < "2025-04-30"]

# Tính tổng
total_temp = df_filtered["temperature_2m"].sum()
total_humidity = df_filtered["relative_humidity_2m"].sum()
total_wind = df_filtered["wind_speed_10m"].sum()

print("Tổng temperature_2m:", total_temp)
print("Tổng relative_humidity_2m:", total_humidity)
print("Tổng wind_speed_10m:", total_wind)
