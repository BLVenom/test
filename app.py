import streamlit as st
import yfinance as yf
import json

ticker = st.text_input("Ticker", "AAPL").upper()

if ticker:
    data = yf.download(ticker, period="5d", interval="1d")
    last_price = data["Close"].iloc[-1]
    
    # Display in Streamlit
    st.metric(f"{ticker} Latest Price", f"${last_price:.2f}")
    
    # Show JSON
    st.json({"ticker": ticker, "last_price": last_price})
