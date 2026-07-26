from flask import Flask, render_template

app = Flask(__name__)

# Dummy product data for now
PRODUCTS = [
    {"id": 1, "name": "Gaming Mouse", "price": 79.99, "category": "Mice", "image": "mouse.jpg", "description": "High precision gaming mouse with RGB lighting", "stock": 15},
    {"id": 2, "name": "Mechanical Keyboard", "price": 149.99, "category": "Keyboards", "image": "keyboard.jpg", "description": "Tactile mechanical switches with RGB backlight", "stock": 8},
    {"id": 3, "name": "HD Webcam", "price": 89.99, "category": "Cameras", "image": "webcam.jpg", "description": "1080p HD webcam with built-in microphone", "stock": 20},
    {"id": 4, "name": "USB-C Hub", "price": 59.99, "category": "Accessories", "image": "hub.jpg", "description": "7-in-1 USB-C hub with HDMI and SD card reader", "stock": 25},
    {"id": 5, "name": "Monitor Stand", "price": 49.99, "category": "Accessories", "image": "stand.jpg", "description": "Adjustable aluminium monitor stand with storage", "stock": 12},
    {"id": 6, "name": "Gaming Headset", "price": 119.99, "category": "Audio", "image": "headset.jpg", "description": "7.1 surround sound gaming headset", "stock": 10}
]

@app.route("/")
def index():
    featured = PRODUCTS[:3]
    return render_template("index.html", products=featured)

@app.route("/products")
def products():
    return render_template("products.html", products=PRODUCTS)

@app.route("/cart")
def cart():
     return render_template ("cart.html")


if __name__ == "__main__":
    app.run(debug=True, port=5002)