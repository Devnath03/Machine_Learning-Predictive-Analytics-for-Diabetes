# Import required libraries
from flask import Flask, request, jsonify  # Flask for API, request for incoming data, jsonify for JSON responses
import joblib  # For loading the saved ML model and scaler

# Initialize Flask application
app = Flask(__name__)

# Load the trained model and scaler from pickle files
model = joblib.load('model.pickle')     # Logistic Regression (or other) model
scaler = joblib.load('scaler.pickle')   # StandardScaler used during training

# Define API endpoint: POST request to /test
@app.route('/test', methods=['POST'])
def home():
    try:
        # Ensure request has JSON body
        if request.is_json:
            data = request.get_json()  # Get JSON data from request body
            print(data)  # Debug: Print received data

            # Extract and convert input features from JSON into a list of floats
            features = [
                float(data['pregnancies']),         # Number of pregnancies
                float(data['glucose']),             # Glucose level
                float(data['bloodpressure']),       # Blood pressure
                float(data['skinthickness']),       # Skin thickness
                float(data['insulin']),              # Insulin level
                float(data['bmi']),                  # Body Mass Index
                float(data['diabetespedigree']),     # Diabetes pedigree function
                float(data['age'])                   # Age of patient
            ]

            print(features)  # Debug: Print features list

            # Apply the same scaling used during model training
            features = scaler.transform([features])

            # Make prediction (0 or 1)
            prediction = model.predict(features)

            # Convert prediction into a human-readable result
            result = "Diabetics" if prediction[0] == 1 else "Non-Diabetics"

            # Return result as JSON
            return jsonify({
                "prediction": result
            })

    except Exception as e:
        # In case of error, return a 400 response
        return jsonify({
            "prediction": "error"
        }), 400

# Run the Flask application in debug mode
if __name__ == '__main__':
    app.run(debug=True)
