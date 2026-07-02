import streamlit as st
import pandas as pd
import pickle
import numpy as np


with open("aqi_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("le_city.pkl", "rb") as f:
    le_city = pickle.load(f)

with open("le_season.pkl", "rb") as f:
    le_season = pickle.load(f)

with open("columns.pkl", "rb") as f:
    feature_cols = pickle.load(f)

st.set_page_config(page_title="AQI Predictor", page_icon="~~~")

st.title("~~~Air Quality Index Predictor~~~")
st.write("Enter the details below to predict the AQI category for an Indian city.")


col1, col2 = st.columns(2)

with col1:
    city = st.selectbox("City", le_city.classes_)
    month = st.slider("Month", 1, 12, 6)
    year = st.selectbox("Year", [2015, 2016, 2017, 2018, 2019, 2020])

with col2:
    pm25 = st.number_input("PM2.5", min_value=0.0, max_value=1000.0, value=60.0, step=0.1)
    pm10 = st.number_input("PM10", min_value=0.0, max_value=1000.0, value=80.0, step=0.1)
    no2 = st.number_input("NO2", min_value=0.0, max_value=200.0, value=30.0, step=0.1)

if st.button("Predict AQI Category", type="primary"):

    # Encode city and season
    city_code = le_city.transform([city])[0]

    def get_season(month):
        if month in [12, 1, 2]:
            return 'Winter'
        elif month in [3, 4, 5]:
            return 'Summer'
        elif month in [6, 7, 8, 9]:
            return 'Monsoon'
        else:
            return 'Post-Monsoon'

    season = get_season(month)
    season_code = le_season.transform([season])[0]

    # Build input dataframe 
    input_data = {col: 0 for col in feature_cols}
    input_data['PM2.5'] = pm25
    input_data['PM10'] = pm10
    input_data['NO2'] = no2
    input_data['Year'] = year
    input_data['Month'] = month
    input_data['City_Code'] = city_code
    input_data['Season_Code'] = season_code

    input_df = pd.DataFrame([input_data])

    # Predict
    prediction_code = model.predict(input_df)[0]
    category_map = {0: 'Good', 1: 'Satisfactory', 2: 'Moderate',3: 'Poor', 4: 'Very Poor', 5: 'Severe'}
    prediction_label = category_map[prediction_code]

    # Show result with color
    color_map = {
        'Good': '🟢', 'Satisfactory': '🟡',
        'Moderate': '🟠', 'Poor': '🔴',
        'Very Poor': '🔴', 'Severe': '⛔'
    }

    st.success(f"### Predicted AQI Category: {color_map[prediction_label]} {prediction_label}")

    if prediction_label in ['Poor', 'Very Poor', 'Severe']:
        st.warning("⚠️ Air quality is hazardous. Avoid outdoor activities.")
    elif prediction_label == 'Moderate':
        st.info("ℹ️ Air quality is moderate. Sensitive groups should be cautious.")

    with st.expander("See your input data"):
        st.dataframe(input_df)


st.markdown("---")
st.caption("Model: Random Forest Classifier · Dataset: India AQI 2015–2020")