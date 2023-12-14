# DEPLOYMENT CODE for monthly_technology
import streamlit as st
import joblib
import pandas as pd
import matplotlib.pyplot as plt

"""
## Welcome to Sales Analytics Hub.
"""

# Load the best model from the pickle file
with open('best_model_technology.pkl', 'rb') as file:
    fb_model_technology = joblib.load(file)

# Input for the number of months for sales prediction
num_of_months = st.number_input('Enter Number of Months Of Sales Prediction')

if st.button("Predict"):
    # LOAD THE DATASET
    monthly_technology_df = pd.read_csv('monthly_technology.csv')
    
    # Convert Date column to time series 
    monthly_technology_df['Order Date'] = pd.to_datetime(monthly_technology_df['Order Date'])
    
    # Set date column as the index
    monthly_technology_df.set_index('Order Date', inplace=True)
    
    # Find the last date in the training data
    last_date_train_technology = monthly_technology_df.index[-1]
    
    # Increment the last date by one month to get the start date for forecasting
    start_date_technology = last_date_train_technology + pd.DateOffset(months=1)
    
    # Create a DataFrame with future dates starting from the next day
    future_technology = pd.DataFrame({'ds': pd.date_range(start=start_date_technology, periods=num_of_months, freq='MS')})
    
    # Generate forecasts
    facebook_pred_technology = fb_model_technology.predict(future_technology)

    # Rename 'ds' as 'Order Date'
    facebook_pred_technology = facebook_pred_technology.rename(columns={'ds': 'Order Date'})
    
    # Set date column as index
    facebook_pred_technology.set_index('Order Date', inplace=True)

    """
    ## Number of Months to be Predicted
    """
    num_of_months

    """
    ## Predicted Sales
    """
    st.write(facebook_pred_technology['yhat'])

    # Plot the forecasted price series
    plt.figure(figsize=(10, 6))
    plt.gca().set_facecolor('lightblue') 
    plt.plot(facebook_pred_technology.index, facebook_pred_technology['yhat'])
    plt.xlabel('Order Date', fontsize=12) 
    plt.ylabel('Predicted Sales', fontsize=12) 
    plt.title('Forecasted Technology Sales', fontsize=15)
    plt.xticks(rotation=45, ha='right') # Rotate xticks
    st.pyplot(plt)  # Display the plot in Streamlit
