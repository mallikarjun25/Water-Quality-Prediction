from flask import Flask, render_template, request, jsonify, url_for
import pandas as pd
import joblib




app = Flask(__name__)
model = joblib.load("svm.pkl")

# Load the dataset
dataset_path = 'C:/Users/user/Desktop/Water-Quality-Prediction/water_potability.csv'
df = pd.read_csv(dataset_path)

# Define a route to get the columns
@app.route('/get_columns', methods=['GET'])
def get_columns():
    columns = list(df.columns)
    return jsonify(columns)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Fetch user inputs from the form
    # input_data = {column: float(request.form.get(column)) for column in df.columns}
    # Perform prediction logic (replace with your actual prediction code)
    #prediction_result = predict_water_quality(input_data)
    if request.method == "POST":
        ph = request.form["ph"]
        hardness = request.form["hardness"]
        solids = request.form["solids"]
        chloramines = request.form["chloramines"]
        sulfate = request.form["sulfate"]
        conductivity = request.form["conductivity"]
        organicCarbon = request.form["organicCarbon"]
        trihalomethanes = request.form["trihalomethanes"]
        turbidity = request.form["turbidity"]

        input_values = [ph, hardness,solids, chloramines, sulfate,conductivity, organicCarbon, trihalomethanes, turbidity]
        input_values = [float(val) for val in input_values]

        prediction = model.predict([input_values])
        return jsonify({'prediction': prediction[0]})

    return render_template('index.html')


# Replace this function with your actual prediction logic
#def predict_water_quality(input_data):
    # Example: If pH is greater than 7, predict good water quality
    #return 'Good Water Quality' if input_data['ph'] > 7 else 'Poor Water Quality'

# @app.route('/ph_val',methods = ["POST"])
# def ph_val():
#     x = float(request.form["ph"])
#     return render_template("result.html", x = x)

# @app.route('/hard_val' ,methods = ["POST"])
# def hard_val():
#     hard = float(request.form["hardness"])
#     return render_template("result.html", hard = hard)

# @app.route('/solids_val' ,methods = ["POST"])
# def solids_val():
#     sol = float(request.form["solids"])
#     return render_template("result.html", sol = sol)

# @app.route('/chl_val' ,methods = ["POST"])
# def chl_val():
#     chlorn = float(request.form["chloramines"])
#     return render_template("result.html", chlorn = chlorn)

# @app.route('/sul_val' ,methods = ["POST"])
# def sul_val():
#     sul = float(request.form["sulfate"])
#     return render_template("result.html", sul = sul)

# @app.route('/con_val' ,methods = ["POST"])
# def con_val():
#     con = float(request.form["conductivity"])
#     return render_template("result.html", con = con)

# @app.route('/org_val' ,methods = ["POST"])
# def org_val():
#     org = float(request.form["organicCarbon"])
#     return render_template("result.html", org = org)

# @app.route('/tri_val' ,methods = ["POST"])
# def tri_val():
#     tri = float(request.form["trihalomethanes"])
#     return render_template("result.html", tri = tri)

# @app.route('/tur_val' ,methods = ["POST"])
# def tur_val():
#     tur = float(request.form["turbidity"])
#     return render_template("result.html", tur = tur)




if __name__ == '__main__':
    app.run(debug=True)
