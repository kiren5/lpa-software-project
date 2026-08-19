from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy stock data
STOCK = [
    {"id": 1, "name": "Gaming Mouse", "quantity": 15, "price": 79.99, "category": "Mice"},
    {"id": 2, "name": "Mechanical Keyboard", "quantity": 8, "price": 149.99, "category": "Keyboards"},
    {"id": 3, "name": "HD Webcam", "quantity": 20, "price": 89.99, "category": "Cameras"},
    {"id": 4, "name": "USB-C Hub", "quantity": 25, "price": 59.99, "category": "Accessories"},
    {"id": 5, "name": "Monitor Stand", "quantity": 12, "price": 49.99, "category": "Accessories"},
    {"id": 6, "name": "Gaming Headset", "quantity": 10, "price": 119.99, "category": "Audio"}
]

# Dummy sales/invoice data
SALES = [
    {"invoice_id": "INV-001", "customer": "John Smith", "item": "Gaming Mouse", "amount": 79.99, "date": "2026-08-01"},
    {"invoice_id": "INV-002", "customer": "Sarah Lee", "item": "Mechanical Keyboard", "amount": 149.99, "date": "2026-08-02"},
    {"invoice_id": "INV-003", "customer": "Mike Chen", "item": "HD Webcam", "amount": 89.99, "date": "2026-08-03"},
    {"invoice_id": "INV-004", "customer": "Emma Wilson", "item": "USB-C Hub", "amount": 59.99, "date": "2026-08-04"}
]

# Dummy system users
USERS = [
    {"id": 1, "name": "Alexander Portacio", "role": "System Administrator", "email": "alex@lpa.com.au"},
    {"id": 2, "name": "Store Manager", "role": "Manager", "email": "manager@lpa.com.au"},
    {"id": 3, "name": "Sales Staff", "role": "Staff", "email": "sales@lpa.com.au"}
]

@app.route("/")
def dashboard():
    total_stock_value = sum(item["quantity"] * item["price"] for item in STOCK)
    total_sales = sum(sale["amount"] for sale in SALES)
    return render_template("dashboard.html", stock_count=len(STOCK), total_stock_value=total_stock_value, sales_count=len(SALES), total_sales=total_sales, user_count=len(USERS))

@app.route("/stock")
def stock():
    return render_template("stock.html", stock=STOCK)

@app.route("/stock/edit/<int:item_id>", methods=["GET", "POST"])
def edit_stock(item_id):
    item = next((i for i in STOCK if i["id"] == item_id), None)
    if request.method == "POST":
        item["quantity"] = int(request.form["quantity"])
        item["price"] = float(request.form["price"])
        return redirect(url_for("stock"))
    return render_template("edit_stock.html", item=item)

@app.route("/stock/add", methods=["GET", "POST"])
def add_stock():
    if request.method == "POST":
        new_id = max(item["id"] for item in STOCK) + 1
        new_item = {
            "id": new_id,
            "name": request.form["name"],
            "quantity": int(request.form["quantity"]),
            "price": float(request.form["price"]),
            "category": request.form["category"]
        }
        STOCK.append(new_item)
        return redirect(url_for("stock"))
    return render_template("add_stock.html")

@app.route("/sales")
def sales():
    return render_template("sales.html", sales=SALES)

@app.route("/admin")
def admin():
    return render_template("admin.html", users=USERS)

if __name__ == "__main__":
    app.run(debug=True, port=5003)