import streamlit as st
import pandas as pd
from model import load_model
from utils import preprocess_input

st.set_page_config(page_title="Real Estate Price Predictor")

st.title("🏠 Real Estate Price Prediction")

st.sidebar.header("Enter House Features")

year_sold = st.sidebar.number_input("Year Sold", min_value=1990, max_value=2025, value=2020)
property_tax = st.sidebar.number_input("Property Tax ($)", min_value=0, value=2500)
insurance = st.sidebar.number_input("Insurance Cost ($)", min_value=0, value=1200)
beds = st.sidebar.slider("Number of Bedrooms", 1, 10, 3)
baths = st.sidebar.slider("Number of Bathrooms", 1, 10, 2)
sqft = st.sidebar.number_input("Living Area (sqft)", min_value=200, max_value=10000, value=1800)
year_built = st.sidebar.number_input("Year Built", min_value=1900, max_value=2025, value=2005)
lot_size = st.sidebar.number_input("Lot Size (sqft)", min_value=500, max_value=50000, value=5000)
basement = st.sidebar.radio("Basement?", [0, 1])
popular = st.sidebar.radio("Popular Location?", [0, 1])
property_age = st.sidebar.number_input("Property Age", min_value=0, max_value=100, value=15)
condo = st.sidebar.radio("Is it a Condo?", [0, 1])
bunglow = st.sidebar.radio("Is it a Bunglow?", [0, 1])

# Prepare input
input_data = preprocess_input(
    year_sold, property_tax, insurance, beds, baths, sqft,
    year_built, lot_size, basement, popular, property_age,
    condo, bunglow
)

# 🛠️ Rename columns to match the trained model exactly
input_data.columns = [
    'year_sold', 'property_tax', 'insurance', 'beds', 'baths', 'sqft',
    'year_built', 'lot_size', 'basement', 'popular', 'property_age',
    'property_type_Bunglow', 'property_type_Condo'
]

model = load_model()

# Optional debug
st.write("🧪 Input feature columns:", input_data.columns.tolist())

# Predict
prediction = model.predict(input_data)

# Display result
st.subheader("🏷️ Predicted House Price:")
st.success(f"${prediction[0]:,.2f}")
