from flask import Flask, render_template, request, jsonify
import pandas as pd
import joblib

app = Flask(__name__)

# Load the SVM model
model = joblib.load("svm.pkl")

# Load the dataset
dataset_path = '/Users/mallikarjunaitha/Documents/GitHub/Water-Quality-Prediction/water_potability.csv'
df = pd.read_csv(dataset_path)

# Define a route to get the columns
@app.route('/get_columns', methods=['GET'])
def get_columns():
    columns = list(df.columns)
    return jsonify(columns)

# Define the main route
@app.route('/')
def index():
    return render_template('index.html')

# Define the prediction route
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == "POST":
        # Fetch user inputs from the form
        ph = float(request.form["ph"])
        hardness = float(request.form["hardness"])
        solids = float(request.form["solids"])
        chloramines = float(request.form["chloramines"])
        sulfate = float(request.form["sulfate"])
        conductivity = float(request.form["conductivity"])
        organicCarbon = float(request.form["organicCarbon"])
        trihalomethanes = float(request.form["trihalomethanes"])
        turbidity = float(request.form["turbidity"])

        # Perform prediction
        input_values = [ph, hardness, solids, chloramines, sulfate, conductivity, organicCarbon, trihalomethanes, turbidity]
        prediction = model.predict([input_values])

        # Return the prediction as JSON
        return jsonify({'prediction': int(prediction[0])})

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
