const slider = document.getElementById('hr-slider');
const manualInput = document.getElementById('manual-input');
const hrDisplay = document.getElementById('hr-display');
const runBtn = document.getElementById('run-btn');
const resultsArea = document.getElementById('results-area');
const scoreVal = document.getElementById('score-val');

// Sync slider and manual input
function updateValue(value) {
    const val = parseFloat(value).toFixed(1);
    slider.value = val;
    manualInput.value = val;
    hrDisplay.textContent = val;
}

slider.addEventListener('input', (e) => {
    updateValue(e.target.value);
});

manualInput.addEventListener('change', (e) => {
    let val = parseFloat(e.target.value);
    if (isNaN(val)) val = 0;
    if (val < 0) val = 0;
    if (val > 12) val = 12;
    updateValue(val);
});

// Handle prediction trigger
runBtn.addEventListener('click', async () => {
    const hours = slider.value;
    
    // UI state feedback
    runBtn.textContent = 'Analyzing Patterns...';
    runBtn.disabled = true;
    resultsArea.classList.add('hidden');
    
    try {
        // Aesthetic delay for "thinking" effect
        await new Promise(resolve => setTimeout(resolve, 800));

        const response = await fetch('/predict', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ study_hours: parseFloat(hours) })
        });
        
        const data = await response.json();
        
        if (response.ok) {
            // Display result with smooth reveal
            scoreVal.textContent = data.predicted_mark;
            resultsArea.classList.remove('hidden');
            
            // Subtle scroll if results are off-screen
            const rect = resultsArea.getBoundingClientRect();
            if (rect.bottom > window.innerHeight) {
                resultsArea.scrollIntoView({ behavior: 'smooth', block: 'center' });
            }
        } else {
            console.error('Prediction error:', data.error);
        }
    } catch (err) {
        console.error('Server connectivity issue:', err);
    } finally {
        runBtn.textContent = 'Predict Score';
        runBtn.disabled = false;
    }
});
