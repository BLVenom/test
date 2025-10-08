import streamlit as st
import yfinance as yf

st.title("📈 Stock Market App")

ticker = st.text_input("Enter Stock Ticker", "AAPL")
data = yf.download(ticker, period="1mo", interval="1d")
st.line_chart(data["Close"])
