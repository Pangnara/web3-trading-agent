# 🚀 Web3 & Trading Intelligence Suite


An all-in-one AI Agent-driven dashboard designed for real-time market insights, intelligent risk management, and interactive Web3 campaign/airdrop tracking.

---

## ✨ Key Features

1. 📊 Live Ticker, Chart & AI Analysis
   - Real-time asset pricing powered by live TradingView widgets.
   - AI-driven technical analysis offering automated entry zones, take-profit (TP) targets, and stop-loss (SL) levels.
   - Market sentiment indicators (Fear & Greed Index, volume metrics, and dominance).

2. ⚖️ Risk & Liquidation Calculator
   - Spot Risk Manager: Calculate exact position sizes, risk percentages, and potential financial risk per trade.
   - Futures Liquidation Calculator: Estimate liquidation thresholds, margin requirements, and leverage exposure (up to 150x) for both Long and Short positions.

3. 🎯 Interactive Web3 Airdrop & Campaign Tracker
   - Interactive checklist to manage daily testnet interactions, smart contract tasks, and governance votes.
   - Real-time progress tracking bar.
   - Built-in form to dynamically add custom airdrop tasks and testnet URLs directly to your dashboard.

---

## 🛠️ Tech Stack
- Python (Core Logic)
- Streamlit (Interactive Web Dashboard Framework)
- TradingView Embed Widgets (Real-time Financial Charts & Tickers)

---

## 🚀 How to Run Locally

If you want to run or test this project locally on your machine, follow these simple steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/Pangnara/web3-trading-agent.git
   cd web3-trading-agent
   ```
2. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Application
   ```bash
   streamlit run app.py
