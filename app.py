from flask import Flask, jsonify, request
import requests

app = Flask(__name__)
API_KEY = '23fa10113efc5efb071a444b3cd0add7'
Base_URL = 'https://api.openweathermap.org/data/2.5/weather'
@app.route('/')
def home():  # put application's code here
    return 'Welcome to the Weather API!'
@app.route('/weather',methods=['GET'])
def get_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({'error': 'Please provide a city name'}), 400
# Call OpenWeatherMap API to get weather data
    try:
        response = requests.get(Base_URL, params={'q': city, 'appid': API_KEY, 'units': 'metric'})
        data = response.json()
        if response.status_code != 200:
            return jsonify({"error": data.get("message","Error fetching weather data")}), response.status_code
        weather_info = {"city":data["name"], "temperature":data["main"]["temp"], "description":data["weather"][0]["description"], "humidity":data["main"]["humidity"], "wind_speed":data["wind"]["speed"]}
        return jsonify(weather_info)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
if __name__ == '__main__':
    app.run(debug=True)
