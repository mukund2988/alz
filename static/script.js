document.getElementById('uploadForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const formData = new FormData(this);

    fetch('/upload', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('resultAlzheimer').innerText = data.message || 'Error uploading image';
    })
    .catch(error => {
        document.getElementById('resultAlzheimer').innerText = 'An error occurred. Please try again.';
    });a
});