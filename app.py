import streamlit as st
import yfinance as yf

st.title("📈 Stock Price Checker")

# Input ticker
ticker = st.text_input("Enter stock ticker", "AAPL").upper()

if ticker:
    try:
        # Download last 5 days data (daily)
        data = yf.download(ticker, period="5d", interval="1d")
        
        if data.empty:
            st.error("No data found for this ticker")
        else:
            # Get the last closing price
            last_price = data["Close"].iloc[-1]
            st.metric(label=f"Latest Price of {ticker}", value=f"${last_price:.2f}")

    except Exception as e:
        st.error(f"Error fetching data: {e}")
