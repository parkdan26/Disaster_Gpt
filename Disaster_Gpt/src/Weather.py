import requests
from Apikey import Key

url = f"https://api.tomorrow.io/v4/timelines?apikey={Key.k}"

params = {
    "location": "43.6532, 79.3832",
    "fields": ["temperature", "humidity", "windSpeed", "precipitationIntensity", "pressureSurfaceLevel",
               "pressureSeaLevel", "cloudCover", "visibility", "uvIndex"],
    "units": "metric",
    "timesteps": ["1d"],
    "startTime": "now",
    "endTime": "nowPlus1d"
}
headers = {
    "accept": "application/json",
    "Accept-Encoding": "gzip",
    "content-type": "application/json"
}

response = requests.post(url, json=params, headers=headers)
data = response.json()

intervals = data['data']['timelines'][0]['intervals']
interval = intervals[len(intervals) - 1]["values"]
temp = interval["temperature"]
humidity = interval["humidity"]
wind_speed = interval["windSpeed"]
precip_intensity = interval["precipitationIntensity"]
pressure_surface = interval["pressureSurfaceLevel"]
pressure_sea = interval["pressureSeaLevel"]
cloud_cover = interval["cloudCover"]
visibility = interval["visibility"]
uv = interval["uvIndex"]

print(response.text)