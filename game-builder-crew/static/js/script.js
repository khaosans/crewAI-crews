function uploadData() {
    const data = document.getElementById('dataInput').value;
    fetch('/upload', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: new URLSearchParams({
            'data': data,
        }),
    })
        .then(response => response.json())
        .then(data => {
            document.getElementById('responseMessage').innerText = data.message;
        })
        .catch(error => {
            document.getElementById('responseMessage').innerText = 'An error occurred';
            console.error('Error:', error);
        });
}
