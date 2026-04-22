# Binance Futures Testnet Trading Bot (Python)

## 📌 Overview
This project is a simplified Python trading bot that places **Market** and **Limit** orders on **Binance Futures Testnet (USDT-M)**.  
It is designed with a clean, reusable structure and includes logging, basic validation, and error handling.

The bot is intended **only for testing and learning purposes** and does **not use real funds**.

---

## ✨ Features
- Place **Market** and **Limit** orders
- Supports **BUY** and **SELL**
- Works with **Binance Futures Testnet (USDT-M)**
- Mock mode for safe testing without API calls
- Structured code (client layer + order logic)
- Error handling and logging support

---

## 🛠 Tech Stack
- Python 3.x
- python-binance
- python-dotenv

---

## 📂 Project Structure
trading_bot/
├── client.py # Binance client setup
├── orders.py # Market & Limit order logic
├── test_order.py # Example usage / testing
├── requirements.txt # Dependencies
├── README.md


> Note: `.env` and `venv/` are intentionally excluded for security reasons.

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone <your-repo-url>
cd trading_bot
2️⃣ Create & Activate Virtual Environment
python3 -m venv venv
source venv/bin/activate
3️⃣ Install Dependencies
pip install -r requirements.txt
```

🔐 Environment Variables

Create a .env file in the project root:

API_KEY=your_binance_testnet_api_key
API_SECRET=your_binance_testnet_api_secret

These should be Binance Futures Testnet credentials, not real account keys.

▶️ How to Run
Example: Test Orders
python test_order.py
This will:

- Create a Binance Futures client
- Place a Market order and a Limit order
- Print the order request and response

🧪 Mock Mode

For safe testing without calling Binance APIs, mock mode is supported in orders.py.

Mock mode returns a simulated order response and is useful when:

- API keys are unavailable
- Network access is restricted

📄 Logging & Error Handling
- API errors and exceptions are handled gracefully
- Logging is implemented for order execution and failures
- Designed to be easily extendable for file-based logging

⚠️ Important Notes
This project uses Binance Futures Testnet
No real trades or real funds are involved
Intended only for assignment evaluation and learning

🚀 Future Improvements 
CLI input using argparse or Typer
Additional order types (Stop-Limit, OCO)
Improved logging configuration
Simple UI or menu-based CLI

👤 Author

Shivangi
(BTech Student | Python & Systems Enthusiast)

✅ Disclaimer

This project is for educational and evaluation purposes only.
It is not financial advice and should not be used for real trading.
Demonstrating logic safely
