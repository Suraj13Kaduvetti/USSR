function goBack() {
    window.location.href = '../Index/index.html';
  }
  
  let userData = {}; // Object to store user data

// This function will be called when the "Fetch User Data" button is clicked
function fetchUserData() {
  // Fetch the user data (this would be done based on actual form input or other source)
  userData = {
    name: document.getElementById('name').value,
    email: document.getElementById('email').value,
    phone: document.getElementById('number').value,
    address: document.getElementById('address').value,
  };

  // Validate if the data is not empty (a simple check for demo purposes)
  if (!userData.name || !userData.email || !userData.phone || !userData.address) {
    document.getElementById('dataMessage').innerText = 'Please fill all fields!';
    return;
  }

  // Update the left side content and display the message
  document.getElementById('dataMessage').innerText = 'Data fetched successfully!';

  // Enable the right section (payment section)
  document.querySelector('.right-section').style.pointerEvents = 'auto';
  document.querySelector('.right-section').style.opacity = '1';

  // Populate the right section with the fetched data
  populatePaymentForm(userData);
}

// This function will populate the payment form inputs on the right section with user data
function populatePaymentForm(data) {
  document.getElementById('payment-info').innerHTML = `
    <h3>Payment Info for ${data.name}</h3>
    <p>Email: ${data.email}</p>
    <p>Phone: ${data.phone}</p>
    <p>Address: ${data.address}</p>
  `;

  // You can also populate the form fields
  document.getElementById('name-right').value = data.name;
  document.getElementById('email-right').value = data.email;
  document.getElementById('number-right').value = data.phone;
  document.getElementById('address-right').value = data.address;
}

// Enable the payment methods section (right section) once data is ready
function enablePaymentSection() {
  const rightSection = document.querySelector('.right-section');
  rightSection.style.pointerEvents = 'auto'; // Enable interaction
  rightSection.style.opacity = '1'; // Make visible
}

