from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
import os

app = Flask(__name__)

# Load the trained model
model_path = 'model.pkl'
if os.path.exists(model_path):
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
else:
    model = None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return jsonify({'error': 'Model not found.'}), 500
    
    try:
        data = request.get_json()
        study_hours = float(data.get('study_hours', 0))
        input_data = np.array([[study_hours]])
        prediction = model.predict(input_data)
        predicted_mark = round(prediction[0][0], 2) if hasattr(prediction[0], '__getitem__') else round(prediction[0], 2)
        
        return jsonify({
            'study_hours': study_hours,
            'predicted_mark': min(max(predicted_mark, 0), 100)
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)
