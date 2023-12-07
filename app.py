from flask import Flask, render_template, request, jsonify, url_for
import pandas as pd
import joblib

app = Flask(__name__)
model = joblib.load("svm.pkl")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict_waterQ', methods=['GET','POST'])
def predict_waterQ():
     # Default prediction value

    ph = float(request.form["ph"])
    hardness = float(request.form["hardness"])
    solids = float(request.form["solids"])
    chloramines = float(request.form["chloramines"])
    sulfate = float(request.form["sulfate"])
    conductivity = float(request.form["conductivity"])
    organicCarbon = float(request.form["organicCarbon"])
    trihalomethanes = float(request.form["trihalomethanes"])
    turbidity = float(request.form["turbidity"])

    input_values = [ph, hardness, solids, chloramines, sulfate, conductivity, organicCarbon, trihalomethanes, turbidity]
    #print(input_values)
        
    prediction = model.predict([input_values]) 
    prediction=prediction[0] # Get the first prediction

    if prediction ==0:
        prediction_new='Unsafe'
    else:
        prediction_new='Safe'

    return render_template('result.html',prediction=prediction_new)

if __name__ == '__main__':
    app.run(debug=True)
