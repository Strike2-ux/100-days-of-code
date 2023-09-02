// shopping_cart.js

let cart = [];

function addToCart(itemName, itemPrice) {
  cart.push({ name: itemName, price: itemPrice });
  updateCartDisplay();
}

function updateCartDisplay() {
  // Logic to update the cart display goes here
  console.log('Cart Contents:', cart);
}
