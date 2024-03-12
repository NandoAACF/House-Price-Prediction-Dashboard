import streamlit as st
import pandas as pd
import pickle
import numpy as np

st.set_page_config(
    page_title="Predict House Price",
    page_icon="📈",
)

def load_model():
    with open('catboostmodel.pickle', 'rb') as file:
        data = pickle.load(file)
    return data

model = load_model()

st.title('📈 Predict House Price')

longitude = st.number_input('Longitude', min_value=-130.0, max_value=-110.0)
latitude = st.number_input('Latitude', min_value=30.0, max_value=45.0)
housing_median_age = st.number_input('House Age', min_value=1, max_value=52)
total_rooms = st.number_input('Total Rooms', min_value=2, max_value=39320)
total_bedrooms = st.number_input('Total Bedrooms', min_value=1, max_value=6445)
population = st.number_input('Population', min_value=3, max_value=35682)
households = st.number_input('Households', min_value=1, max_value=6082)
median_income = st.number_input('Median Income (in thousand USD)', min_value=0.5, max_value=15.0)
ocen_proximity = st.selectbox('Ocean Proximity', ['<1H OCEAN', 'INLAND', 'ISLAND', 'NEAR BAY', 'NEAR OCEAN'])
if ocen_proximity == '<1H OCEAN':
    ocen_proximity = 0
elif ocen_proximity == 'INLAND':
    ocen_proximity = 1
elif ocen_proximity == 'ISLAND':
    ocen_proximity = 2
elif ocen_proximity == 'NEAR BAY':
    ocen_proximity = 3
else:
    ocen_proximity = 4

predict = st.button('Predict')

if predict:
    data = np.array([longitude, latitude, housing_median_age, total_rooms, total_bedrooms, population, households, median_income, ocen_proximity]).reshape(1, -1)
    prediction = model.predict(data)
    result = str(int(round(prediction[0], 2)))
    st.write(f"<h3>Predicted House Price: <span style='color: green'>{result} </span> USD</h3>", unsafe_allow_html=True)