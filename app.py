import streamlit as st
import pickle

# Load the model and preprocesser from pickle files
with open("dtr.pkl", "rb") as model_file:
    model = pickle.load(model_file)

with open("preprocesser.pkl", "rb") as preprocessor_file:
    preprocesser = pickle.load(preprocessor_file)

# Title of the app
st.title("Crop Yield Prediction Per Country")

# Subtitle
st.subheader("Input All Features Here")

# Input fields
year = st.number_input("Year", min_value=1900, max_value=2100, value=2023)
average_rain_fall_mm_per_year = st.number_input("average_rain_fall_mm_per_year", min_value=0.0, value=0.0)
pesticides_tonnes = st.number_input("pesticides_tonnes", min_value=0.0, value=0.0)
avg_temp = st.number_input("avg_temp", min_value=-50.0, max_value=50.0, value=0.0)
area = st.text_input("Area")
item = st.text_input("Item")

# Prediction button
if st.button("Predict"):
    # Create a DataFrame or appropriate input format for your model
    import pandas as pd
    input_data = pd.DataFrame({
        'Year': [year],
        'average_rain_fall_mm_per_year': [average_rain_fall_mm_per_year],
        'pesticides_tonnes': [pesticides_tonnes],
        'avg_temp': [avg_temp],
        'Area': [area],
        'Item': [item]
    })

    # Preprocess the input data
    preprocessed_data = preprocesser.transform(input_data)

    # Make the prediction
    prediction = model.predict(preprocessed_data)

# Display the prediction
    st.write(f"Predicted Yield: {prediction[0]}")
