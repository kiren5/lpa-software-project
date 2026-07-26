// LPA Shopping Cart
let cart = [];

function addToCart(name, price) {
    cart.push({ name: name, price: price });
    updateCartCount();
    showNotification(name);
}

function updateCartCount() {
    const countEl = document.getElementById('cart-count');
    if (countEl) {
        countEl.textContent = cart.length;
    }
}

function showNotification(name) {
    const notification = document.createElement('div');
    notification.style.cssText = `
        position: fixed;
        bottom: 30px;
        right: 30px;
        background-color: #ffd700;
        color: #0a0e2e;
        padding: 15px 25px;
        border-radius: 8px;
        font-weight: bold;
        z-index: 1000;
    `;
    notification.textContent = '✓ ' + name + ' added to cart!';
    document.body.appendChild(notification);
    setTimeout(() => notification.remove(), 2500);
}