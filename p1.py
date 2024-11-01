import pandas as pd
import yfinance as yf
import streamlit as st
import plotly.express as px

st.header("Stock Price Prediction")

with st.sidebar:
    ticker = st.text_input("Stock Ticker")
    button_search = st.button("Search")

    st.subheader("Quick Search for Popular Stocks")
    if st.button("Apple (AAPL)"):
        ticker = "AAPL"
    if st.button("Google (GOOGL)"):
        ticker = "GOOGL"
    if st.button("Microsoft (MSFT)"):
        ticker = "MSFT"

    From = st.date_input("Select Start Date")
    To = st.date_input("Select End Date")
    st.subheader("Need Help?")
    st.write("Enter a valid stock ticker symbol, like 'AAPL' for Apple or 'GOOGL' for Google.")
      

if not ticker:
    st.write("Enter a stock ticker in the sidebar to view stock price predictions.")
else:
    if button_search or ticker:
        # Fetching the data
        data = yf.download(ticker, start = From, end=To)

        # Check if data is retrieved
        if data.empty:
            st.error("No data found for the entered ticker. Please try again.")
        else:
            # Line chart of Adjusted Close price
            fig = px.line(data, x=data.index, y=data["Adj Close"], title=f"{ticker} Stock Price")
            st.plotly_chart(fig)
            
            # Display statistical summary of the data
            st.subheader(f"{ticker} - Key Statistics")
            st.table(data.describe())
