# 🌍 Climate & Weather Intelligence System

A Python-based project that combines an interactive weather dashboard with a machine learning-based temperature prediction and climate risk estimation application. Built using Streamlit, Pandas, Scikit-learn, Matplotlib, and the Open-Meteo API.

## 📌 Project Overview

This project explores two related applications:

1. **Weather Dashboard:** Fetches weather forecast data from the Open-Meteo API and displays current weather conditions, hourly temperature trends, wind speed, precipitation, and multi-day forecasts for selected locations in India.
2. **Climate Risk & Impact Prediction System:** Uses a trained machine learning model and rule-based logic to estimate temperature, classify climate risk levels, and display potential environmental impacts.

The project demonstrates practical applications of Python programming, machine learning, API integration, data processing, and interactive data visualization.

## ✨ Features

### 🌦️ Weather Dashboard

- Current temperature, weather conditions, and wind speed.
- City selection for multiple Indian cities.
- Custom location selection using latitude and longitude.
- Hourly temperature forecasts and weather icons.
- Multi-day weather forecast summaries.
- Temperature trend visualization using Matplotlib.
- Weather data retrieval through the Open-Meteo API.
- Streamlit caching to reduce repeated API requests.
- Interactive dashboard with custom styling.

### 🤖 Machine Learning Model

- Uses the Seattle Weather dataset for model training.
- Predicts maximum temperature (`temp_max`).
- Uses Random Forest Regression.
- Processes missing values in the selected features and target.
- Splits the dataset into training and testing sets.
- Applies StandardScaler to input features.
- Evaluates the model using RMSE and R² score.
- Saves the trained model and scaler using Joblib.
- Exports actual and predicted values for further analysis.

### 🌡️ Climate Risk & Impact Prediction

- Selectable regions, including Delhi, Mumbai, Chennai, Kolkata, and Bengaluru.
- Low, medium, and high emission scenario options.
- Year and rainfall input controls.
- Temperature prediction through a trained model.
- Rule-based climate risk classification: Moderate, High, and Extreme.
- Displays potential impacts related to heat stress, water demand, outdoor activities, and agriculture.

**Note:** The climate risk application is an educational prototype. Its predictions depend on the model, input features, and manually defined regional adjustments and risk thresholds.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Interactive web applications |
| Pandas | Data processing and manipulation |
| NumPy | Numerical computations |
| Scikit-learn | Machine learning, preprocessing, and evaluation |
| Matplotlib | Data visualization |
| Requests | API requests |
| Joblib | Saving and loading trained models |
| Open-Meteo API | Weather forecast data |

## 📂 Project Structure

```text
Climate-Weather-Project/
│
├── app.py
├── weather_dashboard.py
├── train_model.py
├── climate_model.py
├── requirements.txt
├── README.md
│
├── seattle-weather.csv
├── climate_model.pkl
├── scaler.pkl
└── predictions.csv
```

*The structure above represents the expected files based on the provided code. Keep only the files that actually exist in your repository.*

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd <your-project-folder>
```

Replace the placeholders with your actual GitHub repository URL and folder name.

### 2. Install dependencies

Make sure Python is installed, then run:

```bash
pip install -r requirements.txt
```

### 3. Prepare the dataset

Place `seattle-weather.csv` in the project directory. The training script uses this dataset to train the temperature prediction model.

### 4. Train the machine learning model

Run:

```bash
python train_model.py
```

The script trains a Random Forest Regressor and generates:

- `climate_model.pkl` — trained machine learning model.
- `scaler.pkl` — fitted feature scaler.
- `predictions.csv` — actual and predicted values from the test dataset.

### 5. Run the Weather Dashboard

```bash
streamlit run weather_dashboard.py
```

The dashboard retrieves weather data from Open-Meteo and displays it in an interactive interface.

### 6. Run the Climate Risk Application

If your climate risk interface is saved as `app.py`, run:

```bash
streamlit run app.py
```

Ensure that the model, scaler, and application use compatible input features and preprocessing before running predictions.

## 🧠 Machine Learning Workflow

The model training pipeline follows these steps:

1. Load the Seattle Weather dataset using Pandas.
2. Select precipitation, minimum temperature, and wind as input features.
3. Select maximum temperature as the prediction target.
4. Remove rows with missing values in the selected columns.
5. Split the data into 80% training and 20% testing sets.
6. Fit StandardScaler on the training features and transform the training and testing features.
7. Train a Random Forest Regressor with 100 estimators.
8. Evaluate predictions using Root Mean Squared Error (RMSE) and the coefficient of determination (R²).
9. Save the trained model, scaler, and test predictions.

## 📊 Model Evaluation

The training script calculates two evaluation metrics:

- **RMSE:** Measures the typical prediction error in the target's units. Lower values generally indicate better predictions.
- **R² Score:** Indicates how well the model explains the variation in the target values. Its interpretation depends on the test data and model performance.

The actual RMSE and R² values are printed when `train_model.py` runs. They should be reported here only after the model has been trained and evaluated.

## 🌐 Data Sources

- **Seattle Weather dataset:** Used for training the temperature prediction model.
- **Open-Meteo API:** Used to retrieve weather forecast information for the Weather Dashboard.

## ⚠️ Limitations

- The machine learning model is trained on Seattle weather data, which may not represent weather patterns in Indian cities.
- The model predicts maximum temperature using precipitation, minimum temperature, and wind; it is not a validated long-term climate forecasting model.
- The climate risk application uses manually defined emission values, regional temperature adjustments, and risk thresholds.
- Climate risk estimates should not be treated as official forecasts, medical advice, or safety guidance.
- Model performance should be validated using appropriate regional datasets before real-world use.

## 🔮 Future Improvements

- Train and validate models using suitable Indian weather datasets.
- Integrate consistent feature inputs and preprocessing across the training and prediction applications.
- Add model evaluation charts and feature importance analysis.
- Improve climate risk categories using scientifically supported criteria.
- Add additional weather indicators and location-based visualizations.
- Deploy the applications online for easier access.

## 🎯 Project Objective

The primary objective is to demonstrate how machine learning, weather APIs, and interactive visualizations can be combined to process environmental data, explore temperature predictions, and communicate potential climate-related risks.

## 👨‍💻 Author

Developed as a Python, machine learning, and data visualization project.

