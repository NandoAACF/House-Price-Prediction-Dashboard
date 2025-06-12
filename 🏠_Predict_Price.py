import streamlit as st
import pandas as pd
import pickle
import numpy as np

st.set_page_config(
    page_title="Predict House Price",
    page_icon="🏠",
)

def load_model():
    with open('catboostmodel.pickle', 'rb') as file:
        data = pickle.load(file)
    return data

model = load_model()

st.title('🏠 Predict House Price')

with st.container(border=True):
    st.info('📢 Untuk keperluan demo, nilai inputan digenerate secara random jika tidak diisi. Tujuannya supaya memudahkan jika ingin mencoba-coba sistem prediksi ini.')

    if "rand_init" not in st.session_state:
        st.session_state.rand_long = np.random.uniform(-124.35, -114.31)
        st.session_state.rand_lat = np.random.uniform(32.54, 41.95)
        st.session_state.rand_age = np.random.randint(1, 52)
        st.session_state.rand_rooms = np.random.randint(600, 39320)
        st.session_state.rand_bedrooms = np.random.randint(200, 6445)
        st.session_state.rand_population = np.random.randint(300, 35682)
        st.session_state.rand_households = np.random.randint(1, 2082)
        st.session_state.rand_income = np.random.uniform(0.5, 15.0)
        st.session_state.rand_ocean_proximity_by_index = np.random.randint(0, 5)
        st.session_state.rand_init = True

    # rand_long = np.random.uniform(-124.35, -114.31)
    longitude = st.number_input('Longitude', min_value=-130.01, max_value=-110.01, value=st.session_state.rand_long)

    # rand_lat = np.random.uniform(32.54, 41.95)
    latitude = st.number_input('Latitude', min_value=30.01, max_value=45.01, value=st.session_state.rand_lat)

    # rand_age = np.random.randint(1, 52)
    housing_median_age = st.number_input('Median house age in the block', min_value=1, max_value=52, value=st.session_state.rand_age)

    # rand_rooms = np.random.randint(600, 39320)
    total_rooms = st.number_input('Total rooms in the block', min_value=2, max_value=39320, value=st.session_state.rand_rooms)

    # rand_bedrooms = np.random.randint(200, 6445)
    total_bedrooms = st.number_input('Total bedrooms in the block', min_value=1, max_value=6445, value=st.session_state.rand_bedrooms)

    # rand_population = np.random.randint(300, 35682)
    population = st.number_input('Population in the block', min_value=3, max_value=35682, value=st.session_state.rand_population)

    # rand_households = np.random.randint(1, 2082)
    households = st.number_input('Households in the block', min_value=1, max_value=6082, value=st.session_state.rand_households)

    # rand_income = np.random.uniform(0.5, 15.0)
    median_income = st.number_input('Median income in the block (in thousand USD)', min_value=0.2, max_value=15.0, value=st.session_state.rand_income, step=0.1)

    # rand_ocean_proximity_by_index = np.random.randint(0, 5)
    ocean_proximity = st.selectbox('Ocean proximity', ['<1H OCEAN', 'INLAND', 'ISLAND', 'NEAR BAY', 'NEAR OCEAN'], index=st.session_state.rand_ocean_proximity_by_index)
    if ocean_proximity == '<1H OCEAN':
        ocean_proximity = 0
    elif ocean_proximity == 'INLAND':
        ocean_proximity = 1
    elif ocean_proximity == 'ISLAND':
        ocean_proximity = 2
    elif ocean_proximity == 'NEAR BAY':
        ocean_proximity = 3
    else:
        ocean_proximity = 4

    col1, col2 = st.columns([0.135, 0.7])

    with col1:
        predict = st.button("🔍 Predict")
    
    with col2:
        if st.button('🔄 Generate Another Random Data'):
            st.session_state.clear()
            st.rerun()

    if predict:
        data = np.array([longitude, latitude, housing_median_age, total_rooms, total_bedrooms, population, households, median_income, ocean_proximity]).reshape(1, -1)
        prediction = model.predict(data)
        result = str(int(round(prediction[0], 2)))
        st.write(f"<h3>Predicted House Price: <span style='color: green'>{result} </span> USD</h3>", unsafe_allow_html=True)
        st.info('📢 Silakan klik tombol "Generate Another Random Data" untuk mencoba variasi inputan lainnya.')