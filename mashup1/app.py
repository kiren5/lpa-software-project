

from flask import Flask, render_template

import requests

app = Flask(__name__)

# Your OpenWeatherMap API key

API_KEY = "3023618a444715ac1d7e2e7ee07c21b8"

# LPA store locations

STORES = [

    {"city": "Brisbane", "country": "AU"},

    {"city": "Sydney", "country": "AU"},

    {"city": "Melbourne", "country": "AU"}

]

def get_weather(city, country):

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={API_KEY}&units=metric"

    response = requests.get(url)

    data = response.json()

    return {

        "city": city,

        "temperature": data["main"]["temp"],

        "description": data["weather"][0]["description"],

        "humidity": data["main"]["humidity"]

    }

@app.route("/")

def index():

    store_weather = []

    for store in STORES:

        weather = get_weather(store["city"], store["country"])

        store_weather.append(weather)

    return render_template("index.html", stores=store_weather)

if __name__ == "__main__":

    app.run(debug=True)