import requests

API_KEY = "ecd87e44247680a5c5b56374a25b53d2"

def get_weather(city):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()

        # Fetch 6-hour rainfall prediction
        rainfall_forecast = data.get("rain", {}).get("6h", 0)

        return {
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "rainfall": rainfall_forecast
        }
    except Exception as e:
        return {"error": str(e)}
