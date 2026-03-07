document.getElementById('loanForm').addEventListener('submit', async (e) => {
    e.preventDefault();

    const formData = new FormData(document.getElementById('loanForm'));
    
    try {
        const response = await fetch('/predict', {
            method: 'POST',
            body: formData
        });

        const data = await response.json();

        if (data.success) {
            displayResult(data);
        } else {
            alert('Error: ' + data.error);
        }
    } catch (error) {
        alert('Error: ' + error.message);
    }
});

function displayResult(data) {
    const resultSection = document.getElementById('result');
    const statusClass = data.prediction === 1 ? 'approved' : 'denied';
    
    document.getElementById('resultStatus').innerHTML = 
        `<span class="${statusClass}">${data.status}</span>`;
    
    document.getElementById('resultConfidence').textContent = 
        `Confidence: ${data.confidence.toFixed(2)}%`;
    
    resultSection.style.display = 'block';
    resultSection.scrollIntoView({ behavior: 'smooth' });
}