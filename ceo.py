import yfinance as yf
import pandas as pd
import numpy as np
import streamlit as st
from sklearn.linear_model import LinearRegression
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.arima.model import ARIMA

def main():
    # Define the Streamlit app title
    st.title("Financial Analysis ")

    # User enters a ticker symbol in the search menu
    search_symbol = st.text_input("Enter a ticker symbol:")

    # Fetch financial data from Yahoo Finance using the entered ticker symbol
    if search_symbol:
        try:
            # Fetch historical financial data
            start_date = '2023-01-01'
            end_date = '2023-08-20'
            financial_data = yf.download(search_symbol, start=start_date, end=end_date)

            # Check if financial data is available
            if financial_data.empty:
                st.error("No financial data available for the entered ticker symbol.")
            else:
                # Exploratory Data Analysis (EDA)
                st.subheader("Exploratory Data Analysis (EDA)")
                st.line_chart(financial_data[['Open', 'Close', 'High', 'Low', 'Volume']])

                # Time Series Analysis - Seasonal Decomposition
                try:
                    result = seasonal_decompose(financial_data['Close'], model='multiplicative', period=30)
                    st.subheader("Time Series Analysis - Seasonal Decomposition of trend")
                    st.line_chart(result.trend)
                    st.subheader("Time Series Analysis - Seasonal Decomposition of seasonality")
                    st.line_chart(result.seasonal)
                    
                except ValueError as e:
                    st.error("Seasonal decomposition could not be performed due to insufficient data.")

                # Regression Analysis
                st.subheader("Regression Analysis")
                if len(financial_data) > 1:  # Check if there is sufficient data for linear regression
                    X = financial_data[['Open', 'Volume']]
                    y = financial_data['Close']
                    model = LinearRegression()
                    model.fit(X, y)
                    predicted_close = model.predict(X)
                    st.write("Coefficient for Open Price:", model.coef_[0])
                    st.write("Coefficient for Volume:", model.coef_[1])
                    st.write("Intercept:", model.intercept_)
                else:
                    st.error("Insufficient data for linear regression analysis.")

                # Forecasting (Using ARIMA)
                forecast_months = 6
                train_data = financial_data['Close'][:-forecast_months]
                test_data = financial_data['Close'][-forecast_months:]
                model_arima = ARIMA(train_data, order=(5, 1, 0))
                model_arima_fit = model_arima.fit()
                forecasted_values = model_arima_fit.forecast(steps=forecast_months)

               
                # Concluding remarks based on analysis
                st.subheader("Concluding Remarks")
                st.write("-" * 40)

                # Regression Analysis Interpretation
                coeff_open = model.coef_[0]
                coeff_volume = model.coef_[1]

                st.write("Regression Analysis:")
                st.write("Coefficient for Open Price:", coeff_open)
                st.write("Coefficient for Volume:", coeff_volume)
                if coeff_open > 0:
                    st.write("Positive correlation between Open Price and Close Price.")
                else:
                    st.write("Negative or no correlation between Open Price and Close Price.")
                if coeff_volume > 0:
                    st.write("Positive correlation between Volume and Close Price.")
                else:
                    st.write("Negative or no correlation between Volume and Close Price.")
                st.write("-" * 20)

                # Interpretation of Data
                st.title("Interpretation of Data")
                average_growth_rate = (financial_data['Close'].iloc[-1] / financial_data['Close'].iloc[0]) - 1
                if average_growth_rate > 0:
                    st.subheader("The company's economic growth is growing over the analysis period.")
                    st.subheader(f"The average growth rate is {average_growth_rate:.2%}.")
                else:
                    st.subheader("The company's economic growth is declining over the analysis period.")
                    st.subheader(f"The average decline rate is {-average_growth_rate:.2%}.")
        except Exception as e:
            st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
