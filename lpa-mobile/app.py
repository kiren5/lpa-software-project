from flask import Flask, render_template

app = Flask(__name__)

STOCK = [
    {"id": 1, "name": "Gaming Mouse", "quantity": 15, "price": 79.99, "category": "Mice"},
    {"id": 2, "name": "Mechanical Keyboard", "quantity": 8, "price": 149.99, "category": "Keyboards"},
    {"id": 3, "name": "HD Webcam", "quantity": 20, "price": 89.99, "category": "Cameras"},
    {"id": 4, "name": "USB-C Hub", "quantity": 25, "price": 59.99, "category": "Accessories"},
    {"id": 5, "name": "Monitor Stand", "quantity": 12, "price": 49.99, "category": "Accessories"},
    {"id": 6, "name": "Gaming Headset", "quantity": 10, "price": 119.99, "category": "Audio"}
]

SALES = [
    {"invoice_id": "INV-001", "customer": "John Smith", "item": "Gaming Mouse", "amount": 79.99, "date": "2026-08-01"},
    {"invoice_id": "INV-002", "customer": "Sarah Lee", "item": "Mechanical Keyboard", "amount": 149.99, "date": "2026-08-02"},
    {"invoice_id": "INV-003", "customer": "Mike Chen", "item": "HD Webcam", "amount": 89.99, "date": "2026-08-03"},
    {"invoice_id": "INV-004", "customer": "Emma Wilson", "item": "USB-C Hub", "amount": 59.99, "date": "2026-08-04"}
]

@app.route("/")
def home():
    total_sales = sum(sale["amount"] for sale in SALES)
    return render_template("home.html", stock_count=len(STOCK), sales_count=len(SALES), total_sales=total_sales)

@app.route("/stock")
def stock():
    return render_template("stock.html", stock=STOCK)

@app.route("/sales")
def sales():
    return render_template("sales.html", sales=SALES)

if __name__ == "__main__":
    app.run(debug=True, port=5004)