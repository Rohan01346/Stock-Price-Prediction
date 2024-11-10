import pandas as pd
import yfinance as yf
import streamlit as st
import plotly.express as px

st.header("Stock Price Prediction")


#Functions


#Sidebar
with st.sidebar:
    
    if 'ticker' not in st.session_state:
        st.session_state.ticker = ''

    ticker = st.text_input("Stock Ticker",value = st.session_state.ticker)
    if(ticker):
        st.session_state.ticker = ticker
    button_search = st.button("Search")

    # From = st.date_input("Select Start Date")
    # To = st.date_input("Select End Date")
    st.subheader("Need Help?")
    st.write("Enter a valid stock ticker symbol, like 'AAPL' for Apple or 'GOOGL' for Google.")
      

if not st.session_state.ticker:
    st.write("Enter a stock ticker in the sidebar to view stock price predictions.")
else:
    if button_search or st.session_state.ticker:
        # Fetching the data
        data = yf.download(ticker) #,start = From, end=To

        # Check if data is retrieved
        if data.empty:
            st.error("No data found for the entered ticker. Please try again.")
        else:
            # Line chart of Adjusted Close price
            fig = px.line(data, x=data.index, y=data["Adj Close"], title=f"{ticker} Stock Price")
            st.plotly_chart(fig)
            
            # Display statistical summary of the data
            st.subheader(f"{ticker} - Key Statistics")
            
            #Download Data
            st.download_button(
                "Download CSV",
                data.to_csv(index=False).encode('utf-8'),
                ticker+" data.csv",
                "text/csv",
                key="download-csv")
            
            st.table(data.describe())

