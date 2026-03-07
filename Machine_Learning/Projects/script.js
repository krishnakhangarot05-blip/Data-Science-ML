// ========== DOM Elements ==========
const form = document.getElementById('predictionForm');
const resultCard = document.getElementById('resultCard');
const priceValue = document.getElementById('priceValue');
const loadingSpinner = document.getElementById('loadingSpinner');
const errorMessage = document.getElementById('errorMessage');
const errorText = document.getElementById('errorText');

// ========== Initialize Sliders ==========
document.addEventListener('DOMContentLoaded', function() {
    // Get all numeric input fields and their corresponding range sliders
    const sliders = [
        'CRIM', 'ZN', 'INDUS', 'NOX', 'RM', 
        'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'LSTAT'
    ];

    sliders.forEach(feature => {
        const input = document.getElementById(feature);
        const range = document.getElementById(`${feature}-range`);

        if (input && range) {
            // Sync range slider to input
            range.addEventListener('input', function() {
                input.value = this.value;
            });

            // Sync input to range slider
            input.addEventListener('input', function() {
                range.value = this.value;
            });
        }
    });

    // Hide result card initially
    resultCard.classList.add('d-none');
});

// ========== Form Submission ==========
form.addEventListener('submit', async function(e) {
    e.preventDefault();

    // Hide previous results and errors
    resultCard.classList.add('d-none');
    errorMessage.classList.add('d-none');
    loadingSpinner.classList.remove('d-none');

    // Collect form data
    const formData = new FormData(form);
    const data = Object.fromEntries(formData);

    // Also include CHAS value
    data.CHAS = document.getElementById('CHAS').value;

    try {
        // Send prediction request
        const response = await fetch('/api/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        const result = await response.json();

        if (result.success) {
            // Display results
            displayResult(result);
        } else {
            // Display error
            showError(result.error || 'Failed to make prediction');
        }
    } catch (error) {
        showError('Network error: ' + error.message);
    } finally {
        loadingSpinner.classList.add('d-none');
    }
});

// ========== Display Result ==========
function displayResult(result) {
    // Update price display
    priceValue.textContent = result.price;

    // Show result card with animation
    resultCard.classList.remove('d-none');

    // Animate price value
    animatePrice(result.price_raw);
}

// ========== Animate Price ==========
function animatePrice(finalPrice) {
    const duration = 800;
    const startTime = Date.now();
    const startValue = 0;

    function animate() {
        const elapsed = Date.now() - startTime;
        const progress = Math.min(elapsed / duration, 1);
        const currentPrice = Math.round(progress * finalPrice);
        
        priceValue.textContent = '$' + currentPrice.toLocaleString() + '.00';

        if (progress < 1) {
            requestAnimationFrame(animate);
        }
    }

    animate();
}

// ========== Show Error ==========
function showError(error) {
    errorText.textContent = error;
    errorMessage.classList.remove('d-none');
}

// ========== Input Validation ==========
document.querySelectorAll('input[type="number"]').forEach(input => {
    input.addEventListener('change', function() {
        const min = parseFloat(this.min);
        const max = parseFloat(this.max);
        const value = parseFloat(this.value);

        // Clamp value between min and max
        if (value < min) {
            this.value = min;
            const range = document.getElementById(`${this.id}-range`);
            if (range) range.value = min;
        } else if (value > max) {
            this.value = max;
            const range = document.getElementById(`${this.id}-range`);
            if (range) range.value = max;
        }
    });
});

// ========== Real-time Prediction on Change (Optional) ==========
let predictionTimeout;

form.addEventListener('change', function() {
    // Optional: Uncomment to enable auto-prediction on input change
    /*
    clearTimeout(predictionTimeout);
    predictionTimeout = setTimeout(() => {
        form.dispatchEvent(new Event('submit'));
    }, 1000);
    */
});

// ========== Keyboard Shortcuts ==========
document.addEventListener('keydown', function(e) {
    // Enter to submit
    if (e.key === 'Enter' && e.ctrlKey) {
        form.dispatchEvent(new Event('submit'));
    }
    
    // Alt+R to reset
    if (e.key === 'r' && e.altKey) {
        e.preventDefault();
        form.reset();
    }
});

// ========== Local Storage (Save recent predictions) ==========
function saveRecentPrediction(data) {
    const recent = JSON.parse(localStorage.getItem('recentPredictions') || '[]');
    recent.unshift({
        timestamp: new Date().toLocaleString(),
        ...data
    });
    
    // Keep only last 10 predictions
    if (recent.length > 10) {
        recent.pop();
    }
    
    localStorage.setItem('recentPredictions', JSON.stringify(recent));
}

// Improve accessibility
document.querySelectorAll('.form-control, .form-select').forEach(input => {
    input.addEventListener('focus', function() {
        this.parentElement.classList.add('focused');
    });

    input.addEventListener('blur', function() {
        this.parentElement.classList.remove('focused');
    });
});
