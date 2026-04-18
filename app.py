import streamlit as st
import numpy as np
import joblib

# Load saved model and encoder
model = joblib.load('rf_model_no_coconut.pkl')
encoder = joblib.load('encoder_no_coconut.pkl')

# Streamlit app
st.title("🌾 Crop Yield Prediction")

# Input widgets
state = st.selectbox("Select State", encoder.categories_[0])
crop = st.selectbox("Select Crop", encoder.categories_[1])
season = st.selectbox("Select Season", encoder.categories_[2])
crop_year = st.number_input("Enter Crop Year", min_value=2000, max_value=2030, value=2026)
area = st.number_input("Enter Area (hectares)", min_value=0.01, max_value=1000.0, value=1.0)

# Predict button
if st.button("Predict Yield"):
    # Encode categorical input
    X_cat = encoder.transform([[state, crop, season]])
    X_num = np.array([[crop_year, area]])
    X_input = np.hstack((X_num, X_cat))
    
    # Predict log yield and convert back to actual
    yield_log = model.predict(X_input)[0]
    predicted_yield = np.exp(yield_log) - 1
    
    st.success(f"Predicted Crop Yield: {predicted_yield:.2f} tonnes/hectare")