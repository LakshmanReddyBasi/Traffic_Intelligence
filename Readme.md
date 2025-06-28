# Traffic Intelligence Prediction System

A machine learning-powered web application that predicts traffic volume based on weather conditions, time, and environmental factors.

## Features

- **Real-time Traffic Prediction**: Predict vehicle count based on multiple input parameters
- **Weather Integration**: Considers temperature, rain, snow, and weather conditions
- **Time-based Analysis**: Incorporates date and time factors for accurate predictions
- **Web Interface**: User-friendly Flask web application
- **Model Information**: View detailed model performance metrics

## Tech Stack

- **Backend**: Python, Flask
- **Machine Learning**: Scikit-learn, Pandas, NumPy
- **Frontend**: HTML, CSS, JavaScript
- **Data Processing**: Pickle for model serialization

## Project Structure

```
TrafficIntelligence/
├── app/
│   ├── app.py            # Main Flask application
│   ├── templates/
│       ├── home.html     # Landing page
│       └── index.html    # Prediction form
├── pkl/
│   ├── best_model.pkl    # Trained ML model
│   ├── scaler.pkl        # Feature scaler
│   └── label_encoder.pkl # Weather label encoder
├── json/
│   ├── columns.json      # Feature columns configuration
│   └── model_info.json   # Model performance metrics
└── README.md             # Project documentation
```

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd TrafficIntelligence
   ```

2. **Install dependencies**
   ```bash
   pip install flask pandas numpy scikit-learn
   ```

3. **Ensure model files exist in correct directories**
   - Pickle files in `/pkl/` folder
   - JSON files in `/json/` folder
   - HTML templates in `/app/templates/` folder

## Usage

1. **Start the application**
   ```bash
   cd app
   python app.py
   ```

2. **Access the web app**
   - Open browser to `http://localhost:5000`
   - Navigate to home page
   - Go to `/predict-form` for predictions

3. **Make predictions**
   - Enter weather conditions (temperature, rain, snow)
   - Select weather type from dropdown
   - Input date and time information
   - Click predict to get traffic volume estimate

## API Endpoints

- `GET /` - Home page
- `GET /predict-form` - Prediction form
- `POST /predict` - Submit prediction request
- `GET /model_info` - View model performance metrics

## Input Parameters

| Parameter | Type | Description | Required |
|-----------|------|-------------|----------|
| temp | float | Temperature in Celsius | Yes |
| rain | float | Rainfall amount | No (default: 0) |
| snow | float | Snowfall amount | No (default: 0) |
| weather | string | Weather condition | No (default: 'Clouds') |
| year | int | Year | No (default: 2024) |
| month | int | Month (1-12) | No (default: 1) |
| day | int | Day (1-31) | No (default: 1) |
| hours | int | Hour (0-23) | No (default: 12) |
| minutes | int | Minutes (0-59) | No (default: 0) |
| seconds | int | Seconds (0-59) | No (default: 0) |

## Model Information

The system uses a trained machine learning model that:
- Processes weather and temporal features
- Applies feature scaling for optimal performance
- Encodes categorical weather data
- Returns traffic volume predictions in vehicles per hour

## Error Handling

- Invalid weather conditions default to 'Clouds'
- Missing parameters use sensible defaults
- Model errors are caught and displayed to users
- Debug information available for troubleshooting

## Development

### Adding New Features
1. Update model training pipeline
2. Regenerate pickle files
3. Update `columns.json` if new features added
4. Test prediction endpoint

### Model Retraining
1. Update training data
2. Retrain model and save new pickle files
3. Update `model_info.json` with new metrics
4. Restart application

## Troubleshooting

**Common Issues:**
- **Model not loading**: Check if pickle files exist in `/pkl/` folder
- **Config not found**: Verify JSON files are in `/json/` folder  
- **Prediction errors**: Verify input data types and ranges
- **Template not found**: Ensure HTML templates are in `/app/templates/` folder

**Debug Mode:**
- Application runs in debug mode by default
- Check console output for detailed error messages
- Debug information displayed on prediction page

## Performance

- Model R² score displayed on startup
- Prediction response time typically < 100ms
- Handles multiple concurrent requests

## Contributing

1. Fork the repository
2. Create feature branch
3. Make changes and test
4. Submit pull request

