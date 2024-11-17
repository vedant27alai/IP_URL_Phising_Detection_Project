from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load your models
try:
    with open('fraud_detection_model.pkl', 'rb') as f:
        fraud_model = pickle.load(f)
    with open('ip_detection_model.pkl', 'rb') as f:
        ip_model = pickle.load(f)
except Exception as e:
    app.logger.error(f"Error loading models: {e}")

@app.route('/')
def index():
    return 'API is running'

# Predict fraud (based on URL)
@app.route('/predict_fraud', methods=['POST'])
def predict_fraud():
    try:
        data = request.json
        url = data.get('url')
        
        if not url:
            return jsonify({'error': 'No URL provided'}), 400
        
        # Predict using the fraud detection model
        features = [url]  # Assumes the model accepts a single feature
        prediction = fraud_model.predict(features)[0]
        
        # Assuming the model returns a label like 'safe' or 'unsafe'
        return jsonify({'prediction': prediction})
    except Exception as e:
        app.logger.error(f"Error during fraud prediction: {e}")
        return jsonify({'error': 'An error occurred during fraud prediction'}), 500

# Predict IP safety
@app.route('/predict_ip', methods=['POST'])
def predict_ip():
    try:
        data = request.json
        ip_address = data.get('ipAddress')
        
        if not ip_address:
            return jsonify({'error': 'No IP address provided'}), 400
        
        # Predict using the IP detection model
        features = [ip_address]  # Assumes the model accepts a single feature
        prediction = ip_model.predict(features)[0]
        
        # Assuming the model returns a label like 'safe' or 'unsafe'
        return jsonify({'prediction': prediction})
    except Exception as e:
        app.logger.error(f"Error during IP prediction: {e}")
        return jsonify({'error': 'An error occurred during IP prediction'}), 500

if __name__ == '__main__':
    app.run(debug=True)
