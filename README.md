# Super-Store-Time-Series-Analysis
![image](https://github.com/YKamari/Super-Store-Time-Series-Analysis/assets/118848352/874f45c0-c29b-4829-a94c-1bd47f278a4c)

**Group 16**
Student Names:
Bedan Njoroge
Yvonne Kamari
Samuel Lumumba

**Project Overview**
**Business Problem**
Superstores face significant challenges in optimizing inventory management and maximizing sales potential within the furniture and office supplies categories.
The lack of accurate sales forecasts, inadequate insights into consumer behavior, and ineffective inventory strategies lead to understocking or overstocking issues, resulting in missed sales opportunities or increased carrying costs.

**Projective Objective**
The objective of this project is to leverage time series analysis techniques, including ARIMA, SARIMA, Facebook Prophet, and LSTM models, on sales data pertaining to furniture, office supplies and technology from the Superstore. The primary goals include:
1. Forecasting Future Sales
2. Identifying Trends, Patterns, and Seasonality
3. Actionable Insights for Inventory Management: Provide actionable insights to optimize inventory levels, ensuring adequate stock availability while minimizing surplus or shortage issues.
4. Enhancing Marketing Strategies: Understand consumer behavior and sales patterns to devise effective marketing strategies targeted at boosting furniture, office supplies and technology sales.
5. Improving Overall Business Performance: Utilize insights derived from the analysis to enhance operational efficiency, profitability, and overall business performance within these specific product categories.

**Dataset**

The Superstore sales dataset is sourced from Tableau https://community.tableau.com/s/question/0D54T00000CWeX8SAL/sample-superstore-sales-excelxls and consists of the following columns, 
1. Order ID: Unique identifier for each order.
2. Order Date: Date when the order was placed.
3. Ship Date: Date when the order was shipped.
4. Ship Mode: Shipping mode used for the order (e.g., First Class, Standard Class, Second Class, Same Day).
5. Customer ID: Unique identifier for each customer.
6. Customer Name: Name of the customer.
7. Segment: Segmentation of customers (Consumer, Corporate, Home Office).
8. Country: Country where the store operates (contains only United States).
9. City: City where the order was shipped.
10. State: State where the order was shipped.
11. Postal Code: Postal code of the shipping address.
12. Region: Geographical region of the United States (e.g., East, West, North, South).
13. Product ID: Unique identifier for each product.
14. Category: Category of the product (Furniture, Office Supplies, Technology).
15. Sub-Category: Sub-category of the product (Bookcases, Chairs, Labels, Tables, Storage, Furnishings, Art, Phones, Binders, Paper, Appliances, Accessories, Copiers, Envelopes, Fasteners, Machines, Supplies).
16. Product Name: Name of the product.
17. Sales: Total sales revenue for the order.
18. Quantity: Quantity of products ordered.
19. Discount: Percentage of discount applied to the order.
20. Profit: Profit generated from the order.

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




