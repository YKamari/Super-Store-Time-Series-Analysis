# DEPLOYMENT CODE
import streamlit as st
import joblib
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import pyplot
import seaborn as sns

"""
## Welcome to Sales Analytics Hub.

"""

with open('best_model.pkl','rb') as file:
    fb_model1 = joblib.load(file)

num_of_months = st.number_input('Enter Number of Months Of Sales Prediction')

if st.button("predict"):
    # LOAD THE DATASET
    monthly_furniture_df = pd.read_csv('furniture_data.csv')
    
    # Convert Date column to time series 
    monthly_furniture_df['Order Date'] = pd.to_datetime(monthly_furniture_df['Order Date'])
    
    # Set date column as the index
    monthly_furniture_df.set_index('Order Date', inplace=True)
    
    # Find the last date in the training data
    last_date_train = monthly_furniture_df.index[-1]
    
    # Increment the last date by one month to get the start date for forecasting
    start_date = last_date_train + pd.DateOffset(months=1)
    
    # Create a DataFrame with future dates starting from the next day
    future = pd.DataFrame({'ds': pd.date_range(start=start_date, periods=num_of_months, freq='MS')})
    
    # Generate forecasts
    facebook_pred1 = fb_model1.predict(future)

    # Rename 'ds' as 'Date'
    facebook_pred1 = facebook_pred1.rename(columns = {'ds': 'Order Date'})
    
    # Set date column as index
    facebook_pred1.set_index('Order Date', inplace=True)

    """
    ## Number of Months to be Predicted
    """
    num_of_months

    """
    ## Predicted Order Prices in USD
    """
    facebook_pred1['yhat']

    # Plot the forecasted price series
    plt.figure(figsize=(10, 6))
    plt.gca().set_facecolor('lightpink') 
    plt.plot(facebook_pred1.index, facebook_pred1['yhat'])
    plt.xlabel('Order Date', fontsize=12) 
    plt.ylabel('Predicted Price in USD', fontsize=12) 
    plt.title('Forecasted Furniture Prices', fontsize=15)
    plt.xticks(rotation=45, ha='right') # Rotate xticks
    st.pyplot(plt)  # Display the plot in Streamlit