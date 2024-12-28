document.getElementById('loginForm').addEventListener('submit', async function(event) {
    event.preventDefault();

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    const data = { username, password };

    try {
        const response = await fetch('/login', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });

        const result = await response.json();
        document.getElementById('result').innerText = result.message;

        if (response.ok) {
            window.location.href = '/detection';
        }
    } catch (error) {
        document.getElementById('result').innerText = 'An error occurred. Please try again.';
    }
});
