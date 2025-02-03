// Retrieve cart from localStorage
let cart = JSON.parse(localStorage.getItem('cart')) || [];

// Display cart items
const cartItemsContainer = document.getElementById('cart-items');
const totalPriceContainer = document.getElementById('total-price');
let totalPrice = 0;

// Function to render cart
function renderCart() {
    cartItemsContainer.innerHTML = '';
    totalPrice = 0;  // Reset total price

    cart.forEach((item, index) => {
        const itemDiv = document.createElement('div');
        itemDiv.classList.add('cart-item');
        itemDiv.innerHTML = `
            <span>${item.name} - $${item.price.toFixed(2)}</span>
            <button onclick="removeFromCart(${index})">Remove</button>
        `;
        cartItemsContainer.appendChild(itemDiv);
        totalPrice += item.price;
    });

    totalPriceContainer.textContent = totalPrice.toFixed(2);
}

// Function to remove item from cart
function removeFromCart(index) {
    cart.splice(index, 1);
    localStorage.setItem('cart', JSON.stringify(cart));
    renderCart(); // Re-render the cart after removing an item
}

// Function to proceed to payment page
function proceedToPayment() {
    if (cart.length === 0) {
        alert("Your cart is empty! Please add items to the cart before proceeding.");
        return;
    }

    // Store cart data and total price in localStorage for the payment page
    localStorage.setItem('cartData', JSON.stringify(cart));
    localStorage.setItem('totalPrice', totalPrice.toFixed(2));

    // Redirect to payment page
    window.location.href = '../Pay/preview.html';
}

// Initial rendering of the cart
renderCart();
