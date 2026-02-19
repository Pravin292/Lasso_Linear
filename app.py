import streamlit as st
import numpy as np
import joblib

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(
    page_title="AI Health Risk Predictor",
    page_icon="🏥",
    layout="centered"
)

# -------------------------------
# Load Model
# -------------------------------
model = joblib.load("model.pkl")

# -------------------------------
# Custom Styling
# -------------------------------
st.markdown("""
    <style>
    .main {
        background-color: #f5f7fa;
    }
    .stButton>button {
        background-color: #0066cc;
        color: white;
        border-radius: 8px;
        height: 3em;
        width: 100%;
        font-size: 16px;
    }
    </style>
""", unsafe_allow_html=True)

# -------------------------------
# Title Section
# -------------------------------
st.title("🏥 AI-Based Health Risk Assessment")
st.write("This tool predicts a patient's overall health risk score based on clinical indicators.")

st.divider()

# -------------------------------
# Layout in Two Columns
# -------------------------------
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", 0, 120, 30)
    bmi = st.number_input("BMI", 10.0, 60.0, 25.0)
    blood_pressure = st.number_input("Blood Pressure", 50, 200, 120)
    cholesterol = st.number_input("Cholesterol", 100, 400, 200)
    glucose = st.number_input("Glucose Level", 50, 300, 100)
    insulin = st.number_input("Insulin Level", 0.0, 500.0, 80.0)

with col2:
    heart_rate = st.number_input("Heart Rate", 40, 200, 72)
    activity_level = st.slider("Activity Level (1-10)", 1, 10, 5)
    diet_quality = st.slider("Diet Quality (1-10)", 1, 10, 5)
    smoking_status = st.selectbox("Smoking Status", ["No", "Yes"])
    alcohol_intake = st.number_input("Alcohol Intake (units/week)", 0.0, 50.0, 2.0)

# Convert smoking status
smoking_status = 1 if smoking_status == "Yes" else 0

st.divider()

# -------------------------------
# Prediction
# -------------------------------
if st.button("🔍 Analyze Health Risk"):

    input_data = np.array([[age, bmi, blood_pressure, cholesterol,
                            glucose, insulin, heart_rate,
                            activity_level, diet_quality,
                            smoking_status, alcohol_intake]])

    prediction = model.predict(input_data)[0]

    st.subheader("📊 Predicted Health Risk Score")
    st.metric(label="Health Risk Score", value=f"{prediction:.2f}")

    # -------------------------------
    # Risk Categorization Logic
    # -------------------------------
    if prediction < 33:
        st.success("🟢 Low Health Risk")
        st.write("Patient shows relatively healthy indicators. Maintain current lifestyle.")
    elif 33 <= prediction < 66:
        st.warning("🟡 Moderate Health Risk")
        st.write("Patient has some risk factors. Lifestyle improvement recommended.")
    else:
        st.error("🔴 High Health Risk")
        st.write("Patient shows significant risk indicators. Medical consultation advised.")

    st.divider()
    st.caption("⚠️ Disclaimer: This tool is for educational purposes only and not a medical diagnosis.")