import pickle
import json
import pandas as pd
import numpy as np
from flask import Flask, request, render_template
import os

app = Flask(__name__)

# File paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PKL_DIR = os.path.join(BASE_DIR, '..', 'pkl')
JSON_DIR = os.path.join(BASE_DIR, '..', 'json')

# Load models
model = pickle.load(open(os.path.join(PKL_DIR, 'best_model.pkl'), 'rb'))
scaler = pickle.load(open(os.path.join(PKL_DIR, 'scaler.pkl'), 'rb'))
label_encoder = pickle.load(open(os.path.join(PKL_DIR, 'label_encoder.pkl'), 'rb'))

# Load configs
with open(os.path.join(JSON_DIR, 'columns.json'), 'r') as f:
    columns = json.load(f)

with open(os.path.join(JSON_DIR, 'model_info.json'), 'r') as f:
    model_info = json.load(f)

print(f"Loaded {model_info['best_model_name']} model")
print(f"Model test R2 score: {model_info['test_scores'][model_info['best_model_name']]['r2']:.4f}")
print(f"Number of features: {len(columns)}")

# Home route
@app.route('/')
def home():
    return render_template('home.html')

# Prediction form
@app.route('/predict-form')
def predict_form():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get inputs
        temp = float(request.form['temp'])
        rain = float(request.form.get('rain', 0))
        snow = float(request.form.get('snow', 0))
        weather = request.form.get('weather', 'Clouds')
        
        # Date inputs
        year = int(request.form.get('year', 2024))
        month = int(request.form.get('month', 1))
        day = int(request.form.get('day', 1))
        hours = int(request.form.get('hours', 12))
        minutes = int(request.form.get('minutes', 0))
        seconds = int(request.form.get('seconds', 0))
        
        # Create features
        feature_dict = {
            'temp': temp,
            'rain': rain, 
            'snow': snow,
            'year': year,
            'month': month,
            'day': day,
            'hours': hours,
            'minutes': minutes,
            'seconds': seconds
        }
        
        # Encode weather
        try:
            weather_encoded = label_encoder.transform([weather])[0]
        except ValueError:
            weather_encoded = label_encoder.transform(['Clouds'])[0]
        
        feature_dict['weather_encoded'] = weather_encoded
        
        # Create DataFrame
        input_df = pd.DataFrame([feature_dict])
        
        # Add missing columns
        for col in columns:
            if col not in input_df.columns:
                input_df[col] = 0
        
        # Match column order
        input_df = input_df[columns]
        
        # Scale features
        input_scaled = scaler.transform(input_df)
        
        # Make prediction
        prediction = model.predict(input_scaled)[0]
        
        # Debug info
        debug_info = f"Weather: {weather} -> {weather_encoded}, Temp: {temp}, Hour: {hours}"
        
        return render_template('index.html', 
                             prediction_text=f'Predicted Traffic Volume: {prediction:.0f} vehicles',
                             debug_info=debug_info)
    
    except Exception as e:
        return render_template('index.html', 
                             prediction_text=f'Error in prediction: {str(e)}')

@app.route('/model_info')
def show_model_info():
    return {
        'model_name': model_info['best_model_name'],
        'test_scores': model_info['test_scores'],
        'features': columns
    }

if __name__ == "__main__":
    print("Starting Traffic Intelligence App...")
    print(f"Model type: {type(model)}")
    print(f"Scaler type: {type(scaler)}")
    print(f"Label encoder classes: {list(label_encoder.classes_)}")
    app.run(debug=True)