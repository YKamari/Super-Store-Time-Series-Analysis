import streamlit as st
import joblib
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import pyplot
import seaborn as sns
from statsmodels.tsa.statespace.sarimax import SARIMAX

"""
## Welcome to Sales Analytics Hub.
"""

# Load the best SARIMA model
with open('best_model_office_supplies.pkl', 'rb') as file:
    sarima_fit_office_supplies = joblib.load(file)

num_of_months = st.number_input('Enter Number of Months Of Sales Prediction')

if st.button("predict"):
    # LOAD THE DATASET
    monthly_office_supplies_df = pd.read_csv('monthly_office_supplies.csv')
    
    # Convert Date column to time series 
    monthly_office_supplies_df['Order Date'] = pd.to_datetime(monthly_office_supplies_df['Order Date'])
    
    # Set date column as the index
    monthly_office_supplies_df.set_index('Order Date', inplace=True)
    
    # Find the last date in the training data
    last_date_train = monthly_office_supplies_df.index[-1]
    
    # Increment the last date by one month to get the start date for forecasting
    start_date = last_date_train + pd.DateOffset(months=1)
    
    # Create a DataFrame with future dates starting from the next day
    future = pd.DataFrame({'ds': pd.date_range(start=start_date, periods=num_of_months, freq='MS')})
    
    # Generate forecasts
    sarima_pred = sarima_fit_office_supplies.predict(start=start_date, end=future['ds'].iloc[-1])

    # Create DataFrame for predicted values
    sarima_pred_df = pd.DataFrame({'Order Date': sarima_pred.index, 'yhat': sarima_pred.values})
    
    # Set date column as index
    sarima_pred_df.set_index('Order Date', inplace=True)

    """
    ## Number of Months to be Predicted
    """
    num_of_months

    """
    ## Predicted Order Prices in USD
    """
    sarima_pred_df['yhat']

    # Plot the forecasted price series
    plt.figure(figsize=(10, 6))
    plt.gca().set_facecolor('lightblue') 
    plt.plot(sarima_pred_df.index, sarima_pred_df['yhat'])
    plt.xlabel('Order Date', fontsize=12) 
    plt.ylabel('Predicted Price in USD', fontsize=12) 
    plt.title('Forecasted Office Supplies Prices', fontsize=15)
    plt.xticks(rotation=45, ha='right') # Rotate xticks
    st.pyplot(plt)  # Display the plot in Streamlit
