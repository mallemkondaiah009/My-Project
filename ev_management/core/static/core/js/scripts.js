// Add form validation
document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('registrationForm');

    form.addEventListener('submit', (event) => {
        const inputs = form.querySelectorAll('input');
        let isValid = true;

        inputs.forEach((input) => {
            if (input.value.trim() === '') {
                isValid = false;
                input.classList.add('is-invalid');
                input.nextElementSibling.textContent = 'This field is required.';
            } else {
                input.classList.remove('is-invalid');
                input.nextElementSibling.textContent = '';
            }
        });

        if (!isValid) {
            event.preventDefault();
        }
    });

    const inputs = form.querySelectorAll('input');
    inputs.forEach((input) => {
        input.addEventListener('input', () => {
            if (input.value.trim() !== '') {
                input.classList.remove('is-invalid');
                input.nextElementSibling.textContent = '';
            }
        });
    });
});
