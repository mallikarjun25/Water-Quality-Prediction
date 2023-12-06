// Function to check if a value is a valid number
function isValidNumber(value) {
    return !isNaN(parseFloat(value)) && isFinite(value);
}

// Function to predict water quality based on user input
function predictWaterQuality() {
    // Fetch input values from the form
    var phValue = document.getElementById('ph').value;
    var hardnessValue = document.getElementById('hardness').value;
    var solidsValue = document.getElementById('solids').value;
    var chloraminesValue = document.getElementById('chloramines').value;
    var sulfateValue = document.getElementById('sulfate').value;
    var conductivityValue = document.getElementById('conductivity').value;
    var organicCarbonValue = document.getElementById('organicCarbon').value;
    var trihalomethanesValue = document.getElementById('trihalomethanes').value;
    var turbidityValue = document.getElementById('turbidity').value;

    // Validate input values
    if (!isValidNumber(phValue) || phValue < 0 || phValue > 14) {
        // Alert the user if pH value is invalid
        alert('Please enter a valid pH value between 0 and 14.');
        return;
    }

    if (!isValidNumber(hardnessValue) || hardnessValue < 0) {
        // Alert the user if hardness value is invalid
        alert('Please enter a valid hardness value greater than or equal to 0.');
        return;
    }
    if (!isValidNumber(solidsValue) || solidsValue < 0) {
        // Alert the user if TDS value is invalid
        alert('Please enter a valid TDS value greater than or equal to 0.');
        return;
    }

    if (!isValidNumber(chloraminesValue) || chloraminesValue < 0) {
        // Alert the user if value is invalid
        alert('Please enter a valid value greater than or equal to 0.');
        return;
    }

    if (!isValidNumber(sulfateValue) || sulfateValue < 0) {
        // Alert the user if value is invalid
        alert('Please enter a valid value greater than or equal to 0.');
        return;
    }

    if (!isValidNumber(conductivityValue) || conductivityValue < 0) {
         // Alert the user if value is invalid
         alert('Please enter a valid value greater than or equal to 0.');
        return;
    }

    if (!isValidNumber(organicCarbonValue) || organicCarbonValue < 0) {
        // Alert the user if value is invalid
        alert('Please enter a valid value greater than or equal to 0.');
        return;
    }

    if (!isValidNumber(trihalomethanesValue) || trihalomethanesValue < 0) {
        // Alert the user if value is invalid
        alert('Please enter a valid value greater than or equal to 0.');
        return;
    }

    if (!isValidNumber(turbidityValue) || turbidityValue < 0) {
        // Alert the user if value is invalid
        alert('Please enter a valid value greater than or equal to 0.');
        return;
    }

    // Perform prediction logic
    const isPotable = phValue >= 6.5 && phValue <= 8.5;
    const predictionResult = isPotable ? 'Potable' : 'Not Potable';

    // Display result
    const resultDiv = document.getElementById('result');
    resultDiv.innerHTML = `<p>Water Quality Prediction Result: ${predictionResult}</p>`;
}
