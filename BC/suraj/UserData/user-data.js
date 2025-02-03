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
                // Hide popup and display user data
                popup.style.display = 'none';
                userDataDiv.style.display = 'block';

                // Fill in user data
                nameSpan.textContent = user.name;
                emailSpan.textContent = user.email;
                phoneSpan.textContent = user.phone;
                addressSpan.textContent = user.address;
            } else {
                // Handle case where no user is found
                errorMessage.textContent = 'User not found with this ID. Please try again.';
                errorMessage.style.display = 'block';
            }
        } catch (error) {
            console.error('Error:', error);
            errorMessage.textContent = 'An error occurred while retrieving data. Please try again.';
            errorMessage.style.display = 'block';
        }
    });
});
