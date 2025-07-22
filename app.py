# app.py
import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load model and encoders
model = joblib.load("rf_model.pkl")
label_encoders = joblib.load("encoders.pkl")

st.title("Employee Salary Prediction App")

with st.form("input_form"):
    age = st.slider("Age", 17, 90, 30)
    workclass = st.selectbox("Workclass", label_encoders['workclass'].classes_)
    fnlwgt = st.number_input("FNLWGT", min_value=10000, max_value=1000000, value=300000)
    education = st.selectbox("Education", label_encoders['education'].classes_)
    edu_num = st.slider("Education Number", 1, 16, 10)
    marital_status = st.selectbox("Marital Status", label_encoders['marital-status'].classes_)
    occupation = st.selectbox("Occupation", label_encoders['occupation'].classes_)
    relationship = st.selectbox("Relationship", label_encoders['relationship'].classes_)
    race = st.selectbox("Race", label_encoders['race'].classes_)
    gender = st.selectbox("Gender", label_encoders['gender'].classes_)
    capital_gain = st.number_input("Capital Gain", 0, 100000)
    capital_loss = st.number_input("Capital Loss", 0, 5000)
    hours_per_week = st.slider("Hours per Week", 1, 100, 40)
    native_country = st.selectbox("Native Country", label_encoders['native-country'].classes_)

    submit = st.form_submit_button("Predict")

if submit:
    input_dict = {
        'age': age,
        'workclass': workclass,
        'fnlwgt': fnlwgt,
        'education': education,
        'educational-num': edu_num,
        'marital-status': marital_status,
        'occupation': occupation,
        'relationship': relationship,
        'race': race,
        'gender': gender,
        'capital-gain': capital_gain,
        'capital-loss': capital_loss,
        'hours-per-week': hours_per_week,
        'native-country': native_country
    }

    input_df = pd.DataFrame([input_dict])

    # Safe encoding
    for col in input_df.columns:
        if col in label_encoders:
            le = label_encoders[col]
            try:
                input_df[col] = le.transform(input_df[col])
            except ValueError as e:
                st.error(f"Invalid input for '{col}': {input_df[col].values[0]}")
                st.stop()

    prediction = model.predict(input_df)[0]
    result = ">50K" if prediction == 1 else "<=50K"
    st.success(f"Predicted Income: {result}")
