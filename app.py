import streamlit as st
import pandas as pd
from model import load_model
from utils import preprocess_input

st.set_page_config(page_title="Real Estate Price Predictor")

st.title("🏠 Real Estate Price Prediction")

st.sidebar.header("Input House Features")

year = st.sidebar.number_input("Year Built", min_value=1900, max_value=2025, value=2000)
beds = st.sidebar.slider("Number of Bedrooms", 1, 10, 3)
baths = st.sidebar.slider("Number of Bathrooms", 1, 10, 2)
stories = st.sidebar.slider("Number of Stories", 1, 5, 2)
garage = st.sidebar.radio("Garage", [0, 1])
area = st.sidebar.number_input("Area (sqft)", min_value=100, max_value=10000, value=2000)
lot = st.sidebar.number_input("Lot Size (sqft)", min_value=100, max_value=20000, value=5000)
pool = st.sidebar.radio("Swimming Pool", [0, 1])
fireplace = st.sidebar.radio("Fireplace", [0, 1])
renovated = st.sidebar.radio("Recently Renovated", [0, 1])
rating = st.sidebar.slider("Neighborhood Rating", 1, 10, 5)
condo = st.sidebar.radio("Is it a Condo?", [0, 1])
bunglow = st.sidebar.radio("Is it a Bunglow?", [0, 1])

input_data = preprocess_input(
    year, beds, baths, stories, garage, area, lot, pool,
    fireplace, renovated, rating, condo, bunglow
)

model = load_model()
prediction = model.predict(input_data)

st.subheader("Predicted House Price:")
st.success(f"${prediction[0]:,.2f}")
