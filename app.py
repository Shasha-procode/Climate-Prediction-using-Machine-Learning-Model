import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load('climate_model.pkl')

# Title
st.title("🌍 Climate Risk & Impact Prediction System")
st.markdown("### Predict Future Climate Risk for India")

# Inputs
# Region selection
region = st.selectbox(
    "Select Region",
    ["Delhi", "Mumbai", "Chennai", "Kolkata", "Bangalore"]

)

# 🌍 CO2 Scenario Selection
scenario = st.selectbox(
    "Select Emission Scenario",
    ["Low Emission 🌱", "Medium Emission ⚖️", "High Emission 🔥"]
)

# Inputs
year = st.slider("Select Year", 2020, 2100, 2030)

rainfall = st.slider("Rainfall (mm)", 500, 2000, 1100)



if st.button("Predict Climate Risk"):

    # 🌍 STEP 1 → Scenario to CO2 mapping (FIRST)
    if scenario == "Low Emission 🌱":
        co2 = 380
    elif scenario == "Medium Emission ⚖️":
        co2 = 420
    else:
        co2 = 500

    # 🧠 STEP 2 → Prediction
    prediction = model.predict(np.array([[year, co2, rainfall]]))[0]

    # 🌍 STEP 3 → Region adjustment
    if region == "Delhi":
        prediction += 1.5
    elif region == "Mumbai":
        prediction += 0.5
    elif region == "Chennai":
        prediction += 1.0
    elif region == "Kolkata":
        prediction += 1.2
    elif region == "Bangalore":
        prediction -= 0.5

    # 👉 Output
    st.write(f"📍 Region Selected: {region}")
    st.success(f"🌡️ Predicted Temperature: {prediction:.2f} °C")

    # 🔥 RISK ENGINE
    if prediction > 35:
        risk = "EXTREME 🔥"
    elif prediction > 30:
        risk = "HIGH ⚠️"
    else:
        risk = "MODERATE ✅"

    st.subheader(f"⚠️ Climate Risk Level: {risk}")

    # 🧠 IMPACT ENGINE
    if prediction > 35:
        impact = """
        - 🚫 Outdoor activities dangerous  
        - 🧠 High risk of heatstroke  
        - 💧 Water demand extremely high  
        - 🌾 Agriculture severely affected  
        """
    elif prediction > 30:
        impact = """
        - ⚠️ Moderate heat stress  
        - 💧 Increased water demand  
        - 🌾 Crop yield may decrease  
        """
    else:
        impact = """
        - ✅ Climate conditions relatively safe  
        - 🌿 Normal daily activities possible  
        """

    st.markdown("### 🧠 Predicted Impact:")
    st.write(impact)

