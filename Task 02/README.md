📈 Task 2: Predict Future Stock Prices (Short-Term)
🧠 Objective
The goal of this task is to build a machine learning model to predict the next day’s closing stock price using historical stock data. This task focuses on short-term stock price forecasting using regression models.

📂 Dataset Used
We used historical stock price data for Apple Inc. (AAPL), fetched using the Yahoo Finance API.

Timeframe: January 2022 to December 2023
Source: yfinance Python library
Features used:
Open
High
Low
Volume
Target variable:
Next day's Close price (calculated using shift(-1))
🤖 Models Applied
Two regression models were applied to predict the next day's closing price:

Linear Regression
A simple, interpretable model assuming linear relationships between features.

Random Forest Regressor
A powerful ensemble model that captures non-linear patterns in data.

📊 Key Results & Findings
Model	Mean Squared Error (MSE)	R² Score
Linear Regression	84.05	0.99
Random Forest	106.26	0.99
Random Forest outperformed Linear Regression, achieving a higher R² score and lower MSE.
The models were able to predict short-term stock price trends with moderate accuracy.
Visual comparison of actual vs predicted closing prices showed that Random Forest captured market fluctuations more effectively.
📌 Skills Applied
Time series data handling
Data preprocessing & feature engineering
Regression modeling
Model evaluation (MSE, R² Score)
Data visualization using Matplotlib
📁 How to Run
Install required libraries:
import yfinance as yf  
import pandas as pd  
import numpy as np  
from sklearn.model_selection import train_test_split  
from sklearn.linear_model import LinearRegression  
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score  
import matplotlib.pyplot as plt
​
