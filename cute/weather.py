import pyowm

owm = pyowm.OWM('YOUR API KEY')  # You MUST provide a valid API key

# Search for current weather in London (Great Britain)
observation = owm.weather_at_place('Dhaka,bn')
w = observation.get_weather()
print(w)

# Weather details
print(w.get_wind())
print(w.get_humidity())
print(w.get_temperature('celsius'))