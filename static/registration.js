document.getElementById('registrationForm').addEventListener('submit', async function(event) {
    event.preventDefault();

    const name = document.getElementById('name').value;
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const email = document.getElementById('email').value;

    const data = { name, username, password, email };

    try {
        const response = await fetch('/register', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });

        const result = await response.json();
        document.getElementById('result').innerText = result.message;

        if (response.ok) {
            window.location.href = '/login';
        }
    } catch (error) {
        document.getElementById('result').innerText = 'An error occurred. Please try again.';
    }
});
