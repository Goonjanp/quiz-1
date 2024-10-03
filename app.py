import streamlit as st
import pandas as pd
import pickle

# Load the trained Lasso model
filename = 'lasso_model.pkl'
loaded_model = pickle.load(open(filename, 'rb'))

# Create a title for your app
st.title('Monthly Revenue Prediction App')

# Create input fields for the features
st.header('Enter the following details')
avg_order_value = st.number_input('Average Order Value')
total_orders = st.number_input('Total Orders')
conversion_rate = st.number_input('Conversion Rate')
customer_lifetime_value = st.number_input('Customer Lifetime Value')
average_order_frequency = st.number_input('Average Order Frequency')
website_traffic = st.number_input('Website Traffic')
marketing_spend = st.number_input('Marketing Spend')
customer_acquisition_cost = st.number_input('Customer Acquisition Cost')
avg_order_value = st.number_input('Average Order Value')
operating_costs = st.number_input('Operating Costs')

# Create a button to trigger prediction
if st.button('Predict'):
  # Create a DataFrame with the input values
  input_data = pd.DataFrame({
      'avg_order_value': [avg_order_value],
      'total_orders': [total_orders],
      'conversion_rate': [conversion_rate],
      'customer_lifetime_value': [customer_lifetime_value],
      'average_order_frequency': [average_order_frequency],
      'website_traffic': [website_traffic],
      'marketing_spend': [marketing_spend],
      'customer_acquisition_cost': [customer_acquisition_cost],
      'avg_order_value': [avg_order_value],
      'operating_costs': [operating_costs]
  })

  # Make the prediction using the loaded model
  prediction = loaded_model.predict(input_data)[0]

  # Display the prediction
  st.subheader('Predicted Monthly Revenue')
  st.write(prediction)
