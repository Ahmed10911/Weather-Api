from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)
API_KEY = '23fa10113efc5efb071a444b3cd0add7'
Base_URL = 'https://api.openweathermap.org/data/2.5/weather'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    if not city:
        return render_template('index.html', error='Please provide a city name')

    try:
        # Call OpenWeatherMap API to get weather data
        response = requests.get(Base_URL, params={'q': city, 'appid': API_KEY, 'units': 'metric'})
        data = response.json()

        if response.status_code != 200:
            return render_template('index.html', error=data.get("message", "Error fetching weather data"))

        # Extract weather data to pass to the template
        weather_info = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"]
        }

        # Render the weather data into the template
        return render_template('weather.html', weather=weather_info)

    except Exception as e:
        return render_template('index.html', error=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
