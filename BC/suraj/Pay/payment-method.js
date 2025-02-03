// Function to show selected payment section
function showSection(section) {
  // Hide all payment sections first
  document.getElementById('cash').style.display = 'none';
  document.getElementById('online').style.display = 'none';
  document.getElementById('crypto').style.display = 'none';

  // Hide all buttons initially
  document.getElementById('cardButton').style.display = 'none';
  document.getElementById('upiButton').style.display = 'none';
  document.getElementById('ethButton').style.display = 'none';
  document.getElementById('btcButton').style.display = 'none';

  // Show the selected section and its buttons
  if (section === 'cash') {
    document.getElementById('cash').style.display = 'block';
  } else if (section === 'online') {
    document.getElementById('online').style.display = 'block';
    // Show online payment buttons
    document.getElementById('cardButton').style.display = 'inline-block';
    document.getElementById('upiButton').style.display = 'inline-block';
  } else if (section === 'crypto') {
    document.getElementById('crypto').style.display = 'block';
    // Show crypto payment buttons
    document.getElementById('ethButton').style.display = 'inline-block';
    document.getElementById('btcButton').style.display = 'inline-block';
  }
}

// On page load, display the default section (e.g., 'cash') by default
document.addEventListener("DOMContentLoaded", function() {
  showSection('cash'); // Default section to show
});


// Show card payment details
function showCardDetails() {
  document.getElementById('cardDetails').style.display = 'block';
  document.getElementById('upiQRCode').style.display = 'none';
}

// Show UPI QR Code
function showUpiQR() {
  document.getElementById('cardDetails').style.display = 'none';
  document.getElementById('upiQRCode').style.display = 'block';
  
  // Load the UPI QR code image (update the path as per your actual QR image location)
  document.getElementById('upiImage').src = 'path/to/your/qr-code-image.png';
}

// Submit card details
function submitCardDetails() {
  let cardNumber = document.getElementById('cardNumber').value;
  let cvv = document.getElementById('cvv').value;
  
  // Hash the last 8 digits of the card number (this is a basic approach; you may want to use a proper hashing library)
  let cardNumberHash = cardNumber.slice(-8);  // Get the last 8 digits
  cardNumberHash = btoa(cardNumberHash); // Base64 encode as an example of simple hashing

  // Display the hashed card number and cvv
  console.log('Card Number (last 8 digits hashed):', cardNumberHash);
  console.log('CVV:', cvv); // In a real application, never log CVV

  // Handle the submission or store data here
  alert('Card details submitted successfully!');
}

// Show Ethereum QR Code
function showEthQR() {
  document.getElementById('ethDetails').style.display = 'block';
  document.getElementById('btcDetails').style.display = 'none';

  // Load the Ethereum QR code image (update path as needed)
  document.getElementById('ethQR').src = 'path/to/your/eth-qr-code.png';

  // Convert amount to ETH and display it (update as needed)
  let amountInUSD = 100; // Example amount, replace with dynamic calculation
  let ethAmount = convertToEth(amountInUSD);
  document.getElementById('ethAmount').textContent = ethAmount.toFixed(4);
}

// Show Bitcoin QR Code
function showBtcQR() {
  document.getElementById('btcDetails').style.display = 'block';
  document.getElementById('ethDetails').style.display = 'none';

  // Load the Bitcoin QR code image (update path as needed)
  document.getElementById('btcQR').src = 'path/to/your/btc-qr-code.png';

  // Convert amount to BTC and display it (update as needed)
  let amountInUSD = 100; // Example amount, replace with dynamic calculation
  let btcAmount = convertToBtc(amountInUSD);
  document.getElementById('btcAmount').textContent = btcAmount.toFixed(6);
}

// Function to convert USD to ETH (example)
function convertToEth(usdAmount) {
  let ethRate = 2000; // Example ETH rate, replace with actual API data
  return usdAmount / ethRate;
}

// Function to convert USD to BTC (example)
function convertToBtc(usdAmount) {
  let btcRate = 40000; // Example BTC rate, replace with actual API data
  return usdAmount / btcRate;
}

// Function to fetch user data
function fetchUserData() {
  // Assuming the user data is available in ../UserData/user-data.html in some JSON format
  fetch('../UserData/user-data.html')
    .then(response => response.text())
    .then(data => {
      // Here you can extract data, assuming it's in a valid format
      // If user data is found, populate the form
      let userData = extractUserData(data); // Define this function based on the data format
      
      if (userData) {
        document.getElementById('name').value = userData.name || '';
        document.getElementById('registeredId').value = userData.registeredId || '';
        document.getElementById('address').value = userData.address || '';
        document.getElementById('number').value = userData.number || '';
        document.getElementById('email').value = userData.email || '';
        document.getElementById('dataMessage').textContent = 'User data fetched successfully.';
      } else {
        document.getElementById('dataMessage').textContent = 'First find the data then enter it here.';
      }
    })
    .catch(error => {
      console.error('Error fetching user data:', error);
      document.getElementById('dataMessage').textContent = 'Error fetching user data.';
    });
}

// Example extraction function, modify according to your actual data format
function extractUserData(data) {
  try {
    // Assuming the data is in JSON format within the HTML, e.g., in a script tag or hidden element
    let parser = new DOMParser();
    let doc = parser.parseFromString(data, 'text/html');
    let userData = JSON.parse(doc.querySelector('#user-data').textContent); // Adjust as per actual format
    return userData;
  } catch (e) {
    return null;
  }
}
