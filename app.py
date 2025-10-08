from flask import Flask, request, jsonify
import yfinance as yf

app = Flask(__name__)

@app.route('/price', methods=['GET'])
def get_price():
    ticker = request.args.get('ticker')
    if not ticker:
        return jsonify({"error": "Please provide a ticker symbol ?ticker=XYZ"}), 400
    
    try:
        stock = yf.Ticker(ticker)
        data = stock.history(period="1d")
        if data.empty:
            return jsonify({"error": "Invalid ticker or no data found"}), 404

        latest_price = data["Close"].iloc[-1]
        return jsonify({"ticker": ticker.upper(), "price": round(latest_price, 2)})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
