# 📈 Stock Price Direction Predictor

A simple and beautiful Machine Learning web app that predicts whether a stock price will go **UP 📈 or DOWN 📉** the next day.

---

## 🚀 Features

- 📊 Real-time stock data using Yahoo Finance  
- 🤖 Machine Learning model (Random Forest)  
- 📈 Interactive charts with Streamlit  
- 🔍 Predict next-day stock direction  
- 🎛️ User input for stock symbol  

---

## 🛠️ Tech Stack

- Python 🐍  
- Pandas & NumPy  
- Scikit-learn  
- Streamlit  
- yFinance
  
---

## ⚙️ Installation

### 1. Clone repo
```bash
git clone https://github.com/your-username/stock-direction-predictor.git
cd stock-direction-predictor

### 2. Create virtual environment
python -m venv .venv

### 3. Activate environment
.\.venv\Scripts\Activate.ps1

### 4. Install dependencies
pip install -r requirements.txt

▶️ Run App
streamlit run app.py

📊 How it works
Collects stock data
Creates features like returns & moving average
Trains ML model
Predicts next-day direction

🎯 Goal
To achieve prediction accuracy higher than 50% (random guess baseline).

📌 Example
Input: AAPL
Output:
📈 UP or 📉 DOWN
Model accuracy

## 📸 Screenshot
![App Screenshot](assets/screenshot.png)
