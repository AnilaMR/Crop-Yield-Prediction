# Crop-Yield-Prediction
This repository contains a machine-learning project aimed at predicting crop yields based on various environmental and agricultural factors. The prediction model is deployed using a Streamlit web application.

#Project Overview
Agricultural productivity is influenced by numerous factors such as rainfall, temperature, and pesticide use. This project leverages these factors to build a predictive model that estimates crop yields for different countries and crops.
#Files and Structure
1. app.py: This file contains the code for the Streamlit web application. It allows users to input relevant features and obtain predictions for crop yields.
2. project.ipynb: This Jupyter notebook details the data preprocessing, exploratory data analysis, and the development of the predictive model.
3. dtr.pkl and preprocesser.pkl: These are the pickled files for the trained Decision Tree Regressor model and the preprocessor, respectively.

#To run this project, you will need the following Python packages:
streamlit
pandas
numpy
seaborn
matplotlib
scikit-learn

#Model Details
The predictive model used in this project is a Decision Tree Regressor. The model was trained on historical crop yield data, and the features were preprocessed to handle various data types and scales.

#Results
The model provides an estimation of crop yields based on the input features. The predictions are displayed directly in the web application after processing the inputs.


