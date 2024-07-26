import streamlit as st
import numpy as np
from utils import pipeline

st.markdown(  
    """  
    <style>  
    .stApp {  
        background-color: #87CEEB; /* Sky Blue */  
    }  
    </style>  
    """,  
    unsafe_allow_html=True,  
)  

try:
    image_path = "docs/ca_housing.png" # Use a local path or URL  
    st.image(image_path, caption='Sample Image')
except:
    pass  

model = pipeline.load_model("models/ca_housing_prices.pkl")

st.title("California :orange[Home Price] Machine Learning Model :house: :chart_with_upwards_trend: :")

with open("text/data_descr.txt", 'r') as f:
    data_descr = f.read()

# Expander (collapsible section) titled "Data Overview"  
with st.expander("Data Overview"):  
    st.write(data_descr)  

# Input fields for the features  
st.header('Input Features')  
  
# Assuming the remaining features are: MedInc, HouseAge, AveRooms, AveBedrms, Population, AveOccup, Price  
MedInc = st.number_input('Median Income in Block ($100,000)', min_value=0.0, max_value=15.0, value=3.0)  
HouseAge = st.number_input('House Age', min_value=0, max_value=100, value=30)  
AveRooms = st.number_input('Number of Rooms', min_value=1, max_value=15, value=5)  
AveBedrms = st.number_input('Number of Bedrooms', min_value=1, max_value=10, value=2)  
Population = st.number_input('Block Population', min_value=0, max_value=50000, value=1000)  
AveOccup = st.number_input('Average House Occupancy', min_value=1, max_value=100, value=3)  

if st.button('Predict', type="primary"):  
    features = np.array([[MedInc, HouseAge, AveRooms, AveBedrms, Population, AveOccup]])
    scaled_features = pipeline.preprocessing(features)
    prediction = model.predict(scaled_features)  
    st.write(f'Predicted House Value: ${prediction[0]*100000:.2f}') 