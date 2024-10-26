import requests

url = "https://api.tomorrow.io/v4/timelines?apikey=ijFRovOSjBLtMQhxz5ooWOHwzfAcrS1N"

params = {
    "location": "43.6532, 79.3832",
    "fields": ["temperature", "humidity", "windSpeed", "precipitationIntensity", "pressureSurfaceLevel",
               "pressureSeaLevel", "cloudCover", "visibility", "uvIndex"],
    "units": "metric",
    "timesteps": ["1d"],
    "startTime": "now",
    "endTime": "nowPlus5d"
}
headers = {
    "accept": "application/json",
    "Accept-Encoding": "gzip",
    "content-type": "application/json"
}

response = requests.post(url, json=params, headers=headers)

print(response.text)

# import requests
#
# url = "https://api.tomorrow.io/v4/weather/timelines"
#
# headers = {"accept": "application/json"}
#
# params = {
#     'location': '43.6532,79.3832',  # Toronto City (latitude,longitude)
#     'fields': ['temperatureApparentAvg'],  # Desired data fields
#     'timesteps': ['1d'],  # Data frequency
#     'units': 'metric',  # Measurement units
#     'apikey': "ijFRovOSjBLtMQhxz5ooWOHwzfAcrS1N",  # Your API key
# }
#
#
# response = requests.get(url, headers=headers, params=params)
#
# print(response.text)


# import requests
#
# # Replace with your API key
# API_KEY = 'your_api_key_here'
# URL = 'https://api.tomorrow.io/v4/timelines'
#
# # Define parameters
# params = {
#     'location': '40.7128,-74.0060',  # New York City (latitude,longitude)
#     'fields': ['temperature', 'precipitation', 'humidity'],  # Desired data fields
#     'timesteps': ['1h'],  # Data frequency
#     'units': 'metric',  # Measurement units
#     'apikey': API_KEY  # Your API key
# }
#
# # Make the request
# response = requests.get(URL, params=params)

# Check the response
# if response.status_code == 200:
#     data = response.json()
#     print(data)
# else:
#     print(f"Error: {response.status_code}, {response.text}")
