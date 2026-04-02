import pandas as pd
import numpy as np
import yfinance as yf
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import streamlit as st

# Page config
st.set_page_config(page_title="Stock Predictor", page_icon="📈", layout="centered")

# Title
st.markdown("<h1 style='text-align: center; color: green;'>📈 Stock Price Predictor</h1>", unsafe_allow_html=True)
st.write("Predict if stock price will go UP or DOWN")

# Sidebar
stock = st.sidebar.text_input("Enter Stock Symbol", "AAPL")
start_date = st.sidebar.date_input("Start Date")
end_date = st.sidebar.date_input("End Date")

# Load data
@st.cache_data
def load_data(stock):
    df = yf.download(stock, start="2020-01-01")
    return df

df = load_data(stock)

# Show data
if st.checkbox("Show Raw Data"):
    st.write(df.tail())

# Feature engineering
df["Return"] = df["Close"].pct_change()
df["SMA"] = df["Close"].rolling(5).mean()
df["Target"] = np.where(df["Close"].shift(-1) > df["Close"], 1, 0)
df.dropna(inplace=True)

# Train model
X = df[["Return", "SMA"]]
y = df["Target"]

X_train, X_test, y_train, y_test = train_test_split(X, y, shuffle=False)

model = RandomForestClassifier()
model.fit(X_train, y_train)

accuracy = model.score(X_test, y_test)

# Show accuracy
st.subheader("Model Accuracy")
st.success(f"{accuracy*100:.2f}%")

# Chart
st.subheader("Stock Price Chart")
st.line_chart(df["Close"])

# Prediction
latest = df.iloc[-1][["Return", "SMA"]].values.reshape(1, -1)
prediction = model.predict(latest)

st.subheader("Prediction")

if prediction[0] == 1:
    st.success("📈 Price will go UP tomorrow")
else:
    st.error("📉 Price will go DOWN tomorrow")