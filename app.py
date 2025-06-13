from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load the model and scaler
model = joblib.load("house_price_model.pkl")
scaler = joblib.load("scaler.pkl")

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        try:
            # Original 13 inputs
            input_order = ['crim','zn','indus','chas','nox','rm','age','dis','rad','tax','ptratio','b','lstat']
            form_values = [float(request.form.get(feature)) for feature in input_order]

            # Compute engineered features
            crim = form_values[0]
            rm = form_values[5]
            lstat = form_values[12]
            log_crim = np.log(crim + 1)
            log_lstat = np.log(lstat + 1)
            rm_squared = rm ** 2

            # Final feature vector (16 features)
            features = form_values + [log_crim, log_lstat, rm_squared]
            features = np.array(features).reshape(1, -1)

            # Scale and predict
            features_scaled = scaler.transform(features)
            prediction = model.predict(features_scaled)[0]
        except Exception as e:
            prediction = f"Error: {e}"
    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
