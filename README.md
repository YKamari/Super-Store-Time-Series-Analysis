
![base-supply-office-products-1600x800px](https://github.com/YKamari/Super-Store-Time-Series-Analysis/assets/133201112/6085c0f2-c6f7-44e0-a634-4f0c1bb38a8c)


# Super-Store-Time-Series-Analysis
![image](https://github.com/YKamari/Super-Store-Time-Series-Analysis/assets/118848352/874f45c0-c29b-4829-a94c-1bd47f278a4c)

**Group 16**
Student Names:
* Bedan Njoroge
* Yvonne Kamari
* Samuel Lumumba

## Business Problem
Superstores face significant challenges in optimizing inventory management and maximizing sales potential within the furniture and office supplies categories.
The lack of accurate sales forecasts, inadequate insights into consumer behavior, and ineffective inventory strategies lead to understocking or overstocking issues, resulting in missed sales opportunities or increased carrying costs.

## Project Objective

The objective of this project is to leverage time series analysis techniques, including ARIMA, SARIMA, Facebook Prophet, and LSTM models, on sales data pertaining to furniture, office supplies and technology from the Superstore. The primary goals include:

1. **Forecasting Future Sales**
2. **Identifying Trends, Patterns, and Seasonality**
3. **Actionable Insights for Inventory Management**: Provide actionable insights to optimize inventory levels, ensuring adequate stock availability while minimizing surplus or shortage issues.
4. **Enhancing Marketing Strategies**: Understand consumer behavior and sales patterns to devise effective marketing strategies targeted at boosting furniture, office supplies and technology sales.
5. **Improving Overall Business Performance**: Utilize insights derived from the analysis to enhance operational efficiency, profitability, and overall business performance within these specific product categories.

## Data Understanding
The [Superstore sales dataset](https://community.tableau.com/s/question/0D54T00000CWeX8SAL/sample-superstore-sales-excelxls) is sourced from Tableau and consists of the following columns,

* __Order ID__: Unique identifier for each order.
* __Order Date__: Date when the order was placed.
* __Ship Date__: Date when the order was shipped.
* __Ship Mode__: Shipping mode used for the order (e.g., First Class, Standard Class, Second Class, Same Day).
* __Customer ID__: Unique identifier for each customer.
* __Customer Name__: Name of the customer.
* __Segment__: Segmentation of customers (Consumer, Corporate, Home Office).
* __Country__: Country where the store operates (contains only United States).
* __City__: City where the order was shipped.
* __State__: State where the order was shipped.
* __Postal Code__: Postal code of the shipping address.
* __Region__: Geographical region of the United States (e.g., East, West, North, South).
* __Product ID__: Unique identifier for each product.
* __Category__: Category of the product (Furniture, Office Supplies, Technology).
* __Sub-Category__: Sub-category of the product (Bookcases, Chairs, Labels, Tables, Storage, Furnishings, Art, Phones, Binders, Paper, Appliances, Accessories, Copiers, Envelopes, Fasteners, Machines, Supplies).
* __Product Name__: Name of the product.
* __Sales__: Total sales revenue for the order.
* __Quantity__: Quantity of products ordered.
* __Discount__: Percentage of discount applied to the order.
* __Profit__: Profit generated from the order.

The time series analysis will particularly emphasize sales data related to furniture and office supplies.

## Project Structure
1. Exploratory Data Analysis (EDA)
2. Modeling - ARIMA, SARIMA, Facebook Prophet & LSTM (Long Short - Term Memory)
3. Model Evaluation
4. Deployment

5. ## Results

6. ### Furniture Sales Forecast

** Furniture Sales  Prediction Using Facebook Prophet**
![Furniture Prophet](https://github.com/YKamari/Super-Store-Time-Series-Analysis/assets/133201112/d9afe5ea-af09-4eb9-9a1f-407a206ed365)

The Facebook Prophet model showcases superior performance compared to the ARIMA, SARIMA and LSTM models. The Facebook Prophet model achieves a notably lower Mean Absolute Error (MAE) of 147.78, indicating better accuracy in point predictions than ARIMA (MAE: 289.54), SARIMA (MAE: 187.30) and LSTM (MAE: 281.59). Similarly, in terms of Root Mean Squared Error (RMSE), the Facebook Prophet model outperforms ARIMA, SARIMA and LSTM with an RMSE of 194.92, signifying its ability to make more precise predictions compared to the other models (ARIMA RMSE: 337.94, SARIMA RMSE: 239.38, LSTM RMSE: 328.61).

** 5 Year Furniture Sales Prediction Using Facebook Prophet**
![Furniture 5 year](https://github.com/YKamari/Super-Store-Time-Series-Analysis/assets/133201112/9eae8714-2a31-44d1-b9a8-e930c585f8f1)

The sales data reveals a recurring trend where sales hit their lowest points in January and February, gradually rising thereafter. Consistently, the highest sales occur in October, November, and December. Moreover, a significant decline in sales occurs around April and mid-year in June.

The forecast accurately mirrors this seasonal pattern, capturing the trend of lower sales at the beginning of the year and an upsurge towards year-end. The forecast also predicts a clear upward trend in sales over the next five years.

## Office Supplies Sales Forecast

** Office Supplies Sales Prediction Using SARIMA**
![Office Supplies SARIMA](https://github.com/YKamari/Super-Store-Time-Series-Analysis/assets/133201112/8fc5a377-e7d0-470f-b9f2-418e1489fea7)

The SARIMA model performs better than both the ARIMA and Facebook Prophet models, as reflected in its lower Mean Absolute Error (MAE) of 206.66 and Root Mean Squared Error (RMSE) of 254.93. The SARIMA model outperforms the ARIMA model, indicating improved accuracy in point predictions and a better fit to the actual data. However, when compared to the LSTM model, SARIMA exhibits higher a higher MAE (LSTM MAE: 194.259) but still lower RMSE.

** 5 Year Office Supplies Sales Prediction Using SARIMA**
![Office Supplies 5 year](https://github.com/YKamari/Super-Store-Time-Series-Analysis/assets/133201112/57dec617-0f42-4c4d-8f90-d22402a227c9)

The sales data displays a recurrent pattern, consistently hitting its lowest points at the start of each year, notably in January and February, and gradually increasing afterward. The peak sales regularly occur towards the year's conclusion, specifically in October, November, and December. Additionally, noticeable decreases in sales are evident around April and mid-year in June.

The forecast accurately captures this inherent seasonality, effectively replicating the trend of reduced sales at the year's onset and an upward trend towards the end of the year.

Looking ahead in the forecast, a distinct upward trajectory in sales is anticipated over the next five years.


### Technology Sales Forecast

** Technology Sales Prediction Using Facebook Prophet**
![Technology Prophet](https://github.com/YKamari/Super-Store-Time-Series-Analysis/assets/133201112/191a3486-f496-4fe3-b4a5-bb2421e465e3)

The Facebook Prophet model displays superior predictive accuracy in technology product sales compared to traditional time series models like ARIMA and SARIMA. With the lowest Mean Absolute Error (MAE) of 260.69, Prophet's predictions closely align with actual values, outperforming both ARIMA (290.73) and SARIMA (289.75). Moreover, Prophet exhibits the smallest Root Mean Squared Error (RMSE) at 347.58, indicating more consistently accurate forecasts compared to ARIMA (401.75) and SARIMA (358.01). These results highlight Prophet's efficiency and reliability in predicting technology sales, establishing its superiority over conventional models.

** 5 Year Furniture Sales Prediction Using Facebook Prophet**
![Technology 5 year](https://github.com/YKamari/Super-Store-Time-Series-Analysis/assets/133201112/1611808b-0a7c-4429-b09f-edb8f56c3057)

The sales data reveals a cyclic pattern, reaching its lowest levels at the start of the year, notably in January and February, then gradually rising. Consistently, peak sales occur towards the year's conclusion, particularly in October, November, and December. Additionally, there is a noticeable decline in sales around April and in June during the middle of the year.

The forecast effectively mirrors this inherent seasonality, precisely reflecting the trend of reduced sales at the beginning of the year and an upsurge towards the end.

In the forecast, there isn't a significant anticipated alteration in sales over the upcoming five years.

## Summary 
The forecasting models (ARIMA, SARIMA, Facebook Prophet, LSTM) showcase varying performances across categories, emphasizing the need for tailored model selection based on the product segment. 

While the project provided valuable insights into sales trends, profitability, and forecasting models' performances, the challenges in optimizing inventory and maximizing sales potential might persist due to inherent complexities in consumer behavior and market dynamics with 100% accuracy.

Leveraging the time series models effectively can help in better inventory management, targeted marketing, and overall performance improvement. However, continuous refinement and adaptation of strategies are crucial to addressing the unpredictability observed in sales trends.

**Total Sales per Segment**
![image](https://github.com/YKamari/Super-Store-Time-Series-Analysis/assets/118848352/fdec14f6-375d-4121-abd0-9fbde4966e7b)

**Total Profit per Segment**
![image](https://github.com/YKamari/Super-Store-Time-Series-Analysis/assets/118848352/b14b7c84-bc9c-4ff4-ada6-f8388c7f695d)

**Total Sales by Category**
![image](https://github.com/YKamari/Super-Store-Time-Series-Analysis/assets/118848352/39916f45-cea5-49a3-bb67-b50b24cde02c)

**Total Profit by Category**
![image](https://github.com/YKamari/Super-Store-Time-Series-Analysis/assets/118848352/6f0db2f5-6977-464e-858f-7f0f57bc328e)

**Total Sales by Sub-Category**
![image](https://github.com/YKamari/Super-Store-Time-Series-Analysis/assets/118848352/44716c3f-b9da-43a5-9058-380392478b2b)

**Top 10 Product Sales**
![image](https://github.com/YKamari/Super-Store-Time-Series-Analysis/assets/118848352/64ab9826-19b9-4381-aa90-d2304a0e3087)

**Top 10 State by Sales** 
![image](https://github.com/YKamari/Super-Store-Time-Series-Analysis/assets/118848352/21e0015e-ba2b-47bb-b9f3-d1f9b4571ad2)

**Methods**
Resampling
Testing for trends
Decomposition
Train-Test Split
Checking for best Arima order
Modeling - ARIMA - Base Model
          SARIMA
          Facebook Prophet
          LSTM
Model Evaluation - using MAE and RSME

**Furniture best predictor model**
![image](https://github.com/YKamari/Super-Store-Time-Series-Analysis/assets/118848352/85019086-9731-436e-9e73-b35b3ef0a7c4)
Facebook Prophet was the best with MAE: 147.78 and RSME: 194.92

**Next 5 years forecast for furniture using Facebook Prophet Model**
![image](https://github.com/YKamari/Super-Store-Time-Series-Analysis/assets/118848352/b782fa33-e384-4efb-a503-cdac1338eb35)

**Office Supplies best predictor model**
![image](https://github.com/YKamari/Super-Store-Time-Series-Analysis/assets/118848352/91a26e1c-0039-4120-8ce2-8ea334af2d29)
SARIMA was the the best with MAE: 206.66 and RSME: 254.93

**Next 5 years forecast for Office Supplies using SARIMA Model**
![image](https://github.com/YKamari/Super-Store-Time-Series-Analysis/assets/118848352/11c780c2-1b26-4978-b820-26b95302f32d)

**Technology best predictor model**
![image](https://github.com/YKamari/Super-Store-Time-Series-Analysis/assets/118848352/2fb33b39-f70b-4403-8b2d-07331cc51eb6)
Facebook was the best with MAE: 260.69 and RSME: 347.58

**Next 5 years forecast for Technology using Facebook Prophet Model**
![image](https://github.com/YKamari/Super-Store-Time-Series-Analysis/assets/118848352/d8e4b8da-cf08-4dc6-8c58-4c25055a8e82)

**LSTM Model Predictor vs Actual Sales**
![image](https://github.com/YKamari/Super-Store-Time-Series-Analysis/assets/118848352/fad38fa3-9a21-4cd4-a428-9b0687921983)


**Recommendations**
- Inventory Management:
Optimize stock levels by increasing inventory during peak seasons and reducing it during off-seasons to minimize carrying costs.
- Marketing Strategies:
Allocate a budget for promotions and discounts during low periods to attract customers and boost sales.
- Product Launches:
Strategically launch new products for the various categories during peak periods to provide customers with a diverse selection.
- Supplier Collaboration:
Collaborate closely with suppliers and logistics partners to meet increased demand during peak periods. Negotiate for favorable terms and discounts to reduce overall costs.

**Overall Business Insights**
- Financial Planning:
Allocate higher budgets for sales and costs during peak periods in financial planning. During low periods, focus on cost reduction strategies.
- Operational Efficiency:
Anticipate increased order fulfillment requirements during peak periods by adjusting stock levels and logistics operations.
- Staffing:
Plan staffing levels to ensure adequate coverage during high seasons and consider optimizing staff costs by implementing leave rotations during low seasons.
- Customer Experience:
Ensure stock availability and provide excellent service during high seasons by properly covering staffing needs and optimizing the overall customer experience.

**Limitations**
- Assumption of Stationarity: 
Time series models often assume stationarity in data, which might not hold true in real-world scenarios, leading to challenges in model application and accuracy.
Seasonal Variations:
- Unforeseen changes in consumer behavior, market trends, or external factors (e.g., economic changes, seasonal fluctuations) might impact sales differently than historical data suggests, affecting the accuracy of forecasts.
- Changing Consumer Behavior:
Behavioral changes in consumers over time might not be captured entirely by historical data, potentially leading to shifts in purchasing patterns that the models may not anticipate accurately.
- Promotions: 
The models do not factor in the effect of promotions in driving sales particularly duiring the holiday seasons.




