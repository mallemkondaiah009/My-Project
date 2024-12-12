document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.getElementById('loginForm');
    const usernameInput = document.getElementById('username');
    const passwordInput = document.getElementById('password');
    const usernameError = document.getElementById('usernameError');
    const passwordError = document.getElementById('passwordError');

    loginForm.addEventListener('submit', (e) => {
        let isValid = true;

        // Reset error messages
        usernameError.textContent = '';
        passwordError.textContent = '';

        // Validate Username
        if (usernameInput.value.trim() === '') {
            usernameError.textContent = 'Username is required.';
            isValid = false;
        }

        // Validate Password
        if (passwordInput.value.trim() === '') {
            passwordError.textContent = 'Password is required.';
            isValid = false;
        }

        // Prevent form submission if validation fails
        if (!isValid) {
            e.preventDefault();
        }
    });
});
