from flask import Flask, request, jsonify
from API import get_prediction

app = Flask(__name__)

# path to trained model
model_path = r"/models/Malicious_URL_Prediction.h5"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()  # Get the JSON data from the request
    url = data['url']  # Extract the URL from the JSON data

    # Make prediction using the get_prediction function
    prediction = get_prediction(url, model_path)

    # Return the prediction as JSON response
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run()
