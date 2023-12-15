# DEPLOYMENT CODE
import joblib
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import pyplot
import seaborn as sns
import streamlit as st

"""
## Welcome to Sales Analytics Hub.

"""

with open('fb_furniture_model.pkl','rb') as file:
    fb_furniture_model = joblib.load(file) 

with open('sarimax_office_model.pkl','rb') as file:
    sarimax_office_model = joblib.load(file)

with open('fb_tech_model.pkl','rb') as file:
    fb_tech_model = joblib.load(file)

num_of_months = st.number_input('Enter Number of Months Of Sales Prediction')

if st.button("predict"):
    # LOAD THE DATASETS
    monthly_furniture_df = pd.read_csv('furniture_data.csv')
    monthly_office_supplies_df = pd.read_csv('office_supplies_data.csv')
    monthly_technology_df = pd.read_csv('technology_data.csv')
    
    # Convert Date column to time series 
    monthly_furniture_df['Order Date'] = pd.to_datetime(monthly_furniture_df['Order Date'])
    monthly_office_supplies_df['Order Date'] = pd.to_datetime(monthly_office_supplies_df['Order Date'])
    monthly_technology_df['Order Date'] = pd.to_datetime(monthly_technology_df['Order Date'])
    
    # Set date column as the index
    monthly_furniture_df.set_index('Order Date', inplace=True)
    monthly_office_supplies_df.set_index('Order Date', inplace=True)
    monthly_technology_df.set_index('Order Date', inplace=True)
    
    # Find the last date in the datasets
    last_date_furniture = monthly_furniture_df.index[-1]
    last_date_office = monthly_office_supplies_df.index[-1]
    last_date_tech = monthly_technology_df.index[-1]
    
    # Increment the last date by one month to get the start date for forecasting
    start_date_furniture = last_date_furniture + pd.DateOffset(months=1)
    start_date_office = last_date_office + pd.DateOffset(months=1)
    start_date_tech = last_date_tech + pd.DateOffset(months=1)
    
    # For furniture and technology, create a DataFrame with future dates starting from the next day
    future_furniture = pd.DataFrame({'ds': pd.date_range(start=start_date_furniture, periods=num_of_months, freq='MS')})
    future_tech = pd.DataFrame({'ds': pd.date_range(start=start_date_tech, periods=num_of_months, freq='MS')})
    # For office supplies, determine the end date
    forecast_end_date_office = start_date_office + pd.DateOffset(months=num_of_months-1)

    # Generate forecasts
    furniture_pred = fb_furniture_model.predict(future_furniture)
    office_pred = sarimax_office_model.predict(start=start_date_office, end=forecast_end_date_office)
    technology_pred = fb_tech_model.predict(future_tech)
    
    # Rename 'ds' as 'Date' in Prophet forecasts
    furniture_pred = furniture_pred.rename(columns = {'ds': 'Order Date'})
    technology_pred = technology_pred.rename(columns = {'ds': 'Order Date'})
    
    # Set date column of furniture prediction as index
    furniture_pred.set_index('Order Date', inplace=True)
    technology_pred.set_index('Order Date', inplace=True)

    # Rename 'yhat' as 'Price' in furniture prediction
    furniture_pred['Furniture'] = furniture_pred['yhat']

    # Filter unnecessary columns in furniture
    sales_prediction = furniture_pred['Furniture'] 

    # Combine predictions with the same index
    combined_predictions = pd.concat([sales_prediction, office_pred, technology_pred['yhat']], axis=1)
    combined_predictions.columns = ['Furniture', 'Office', 'Technology']


    """
    ## Number of Months to be Predicted
    """
    num_of_months

    """
    ## Predicted Sales 
    """
    combined_predictions

    # Plotting the combined predictions
    plt.figure(figsize=(10, 6))
    plt.plot(combined_predictions.index, combined_predictions['Furniture'], label='Furniture', color='blue')
    plt.plot(combined_predictions.index, combined_predictions['Office'], label='Office', color='green')
    plt.plot(combined_predictions.index, combined_predictions['Technology'], label='Technology', color='red')

    plt.xlabel('Order Date', fontsize=12)
    plt.ylabel('Sales', fontsize=12)
    plt.title('Forecasted Store Sales', fontsize=15)
    plt.xticks(rotation=45, ha='right')
    plt.legend()
    plt.tight_layout()

    # Display the plot in Streamlit
    st.pyplot(plt)