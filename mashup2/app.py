from flask import Flask, render_template
import requests

app = Flask(__name__)

EXCHANGE_API_KEY = "1d453d10ad794491af929469"

PRODUCTS = [
    {"name": "Gaming Mouse", "price_aud": 79.99},
    {"name": "Mechanical Keyboard", "price_aud": 149.99},
    {"name": "HD Webcam", "price_aud": 89.99},
    {"name": "USB-C Hub", "price_aud": 59.99},
    {"name": "Monitor Stand", "price_aud": 49.99}
]

def get_exchange_rates():
    url = f"https://v6.exchangerate-api.com/v6/{EXCHANGE_API_KEY}/latest/AUD"
    response = requests.get(url)
    data = response.json()
    return data["conversion_rates"]

@app.route("/")
def index():
    rates = get_exchange_rates()
    products = []
    for product in PRODUCTS:
        products.append({
            "name": product["name"],
            "aud": product["price_aud"],
            "usd": round(product["price_aud"] * rates["USD"], 2),
            "eur": round(product["price_aud"] * rates["EUR"], 2),
            "gbp": round(product["price_aud"] * rates["GBP"], 2)
        })
    return render_template("index.html", products=products)

if __name__ == "__main__":
    app.run(debug=True, port=5001)