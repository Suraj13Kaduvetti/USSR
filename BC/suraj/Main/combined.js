document.addEventListener('DOMContentLoaded', () => {
    const popup = document.getElementById('popup');
    const submitButton = document.getElementById('submit-id');
    const regIdInput = document.getElementById('reg-id');
    const errorMessage = document.getElementById('error-message');
    const userDataDiv = document.getElementById('user-data');
    const nameSpan = document.getElementById('name');
    const emailSpan = document.getElementById('email');
    const phoneSpan = document.getElementById('phone');
    const addressSpan = document.getElementById('address');
  
    // Function to fetch user data
    async function fetchUserData() {
      try {
        const response = await fetch('../JSON/userData.json');
        if (!response.ok) {
          throw new Error(`Failed to fetch: ${response.status} ${response.statusText}`);
        }
        const users = await response.json();
        return users;
      } catch (error) {
        console.error('Error fetching user data:', error.message);
        alert('Failed to load user data. Check the console for more details.');
      }
    }
  
    // Function to show the user data and payment options
    function showUserData(user) {
      // Hide the popup and show the user data section
      popup.style.display = 'none';
      userDataDiv.style.display = 'block';
  
      // Fill in user data
      nameSpan.textContent = user.name;
      emailSpan.textContent = user.email;
      phoneSpan.textContent = user.phone;
      addressSpan.textContent = user.address;
  
      // Now show the payment section
      showSection('cash');  // Default section to show
    }
  
    // Event listener for the submit button
    submitButton.addEventListener('click', async () => {
      const regId = regIdInput.value.trim();
      if (!regId) {
        errorMessage.textContent = 'Please enter a registration ID.';
        errorMessage.style.display = 'block';
        return;
      }
  
      try {
        const users = await fetchUserData();
        const user = users.find(u => u.registration_id === regId);
  
        if (user) {
          // User found, show the data and payment sections
          showUserData(user);
        } else {
          errorMessage.textContent = 'User not found with this ID. Please try again.';
          errorMessage.style.display = 'block';
        }
      } catch (error) {
        console.error('Error:', error);
        errorMessage.textContent = 'An error occurred while retrieving data. Please try again.';
        errorMessage.style.display = 'block';
      }
    });
  
    // Function to show selected payment section
    function showSection(section) {
      document.getElementById('cash').style.display = 'none';
      document.getElementById('online').style.display = 'none';
      document.getElementById('crypto').style.display = 'none';
  
      if (section === 'cash') {
        document.getElementById('cash').style.display = 'block';
        populateForm('cash');
      } else if (section === 'online') {
        document.getElementById('online').style.display = 'block';
        populateForm('online');
      } else if (section === 'crypto') {
        document.getElementById('crypto').style.display = 'block';
        populateForm('crypto');
      }
    }
  
    // Function to populate form fields with user data
    function populateForm(section) {
      const user = {
        name: nameSpan.textContent,
        email: emailSpan.textContent,
        phone: phoneSpan.textContent,
        address: addressSpan.textContent
      };
  
      document.getElementById(`${section}-name`).value = user.name;
      document.getElementById(`${section}-email`).value = user.email;
      document.getElementById(`${section}-number`).value = user.phone;
      document.getElementById(`${section}-address`).value = user.address;
      document.getElementById(`${section}-registeredId`).value = regIdInput.value;
    }
  
    // Default behavior when page loads
    showSection('cash'); // Show the default payment section
  });
  