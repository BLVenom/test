import streamlit as st
import yfinance as yf

st.set_page_config(page_title="Trading Bot Dashboard", layout="centered")
st.title("📊 Trading Bot Summary")

# Input: Ticker symbol
ticker = st.text_input("Enter stock ticker", "AAPL").upper()

if ticker:
    try:
        # Download last 5 days of data
        data = yf.download(ticker, period="5d", interval="1d", progress=False)

        # Check if data is valid
        if data.empty or "Close" not in data.columns:
            st.error("No valid data found for this ticker.")
        else:
            # Get last closing price safely
            last_price = float(data["Close"].iloc[-1])

            # Simple momentum logic: Buy if price increased from yesterday, else Sell
            signal = "BUY" if last_price > float(data["Close"].iloc[-2]) else "SELL"

            # Display metrics
            st.metric(label=f"{ticker} Latest Price", value=f"${last_price:.2f}",
                      delta=f"${last_price - float(data['Close'].iloc[-2]):.2f}")
            st.write(f"**Signal:** {signal}")

            # Optional: Show recent price history
            st.subheader("Last 5 Days Prices")
            st.dataframe(data[["Close"]].round(2))

    except Exception as e:
        st.error(f"Error fetching data: {e}")
