function predictWaterQuality() {
    // Fetch input values
    const phValue = document.getElementById('ph').value;
    // Fetch other input values

    // Perform prediction logic
    const predictionResult = phValue > 7 ? 'Potable' : 'Not Potable';

    // Display result
    const resultDiv = document.getElementById('result');
    resultDiv.innerHTML = `<p>Water Quality Prediction Result: ${predictionResult}</p>`;
}
