// Initialize an empty cart
let cart = [];

// Function to add products to the cart
function addToCart(productName, productPrice) {
    // Push product to cart
    cart.push({ name: productName, price: productPrice });

    // Store the cart in localStorage
    localStorage.setItem('cart', JSON.stringify(cart));

    alert(productName + ' has been added to your cart!');
}
