import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

from statsmodels.tsa.arima.model import ARIMA
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

# Title
st.title("📈 Time Series Stock Prediction (AR, MA, ARMA, ARIMA)")

# Sidebar
st.sidebar.header("Stock Settings")

stock = st.sidebar.text_input("Enter Stock Symbol", "RELIANCE.NS")
start = st.sidebar.date_input("Start Date", pd.to_datetime("2020-01-01"))
end = st.sidebar.date_input("End Date", pd.to_datetime("2024-01-01"))

model_choice = st.sidebar.selectbox(
    "Select Model",
    ["AR", "MA", "ARMA", "ARIMA"]
)

# Load data
data = yf.download(stock, start=start, end=end)

if not data.empty:

    close = data["Close"]

    st.subheader("📄 Raw Data")
    st.write(close.tail())

    # -----------------------
    # Plot Original Data
    # -----------------------
    st.subheader("📊 Stock Price")

    fig, ax = plt.subplots()
    ax.plot(close, label="Close Price")
    ax.legend()
    st.pyplot(fig)

    # -----------------------
    # ACF & PACF
    # -----------------------
    st.subheader("📉 ACF & PACF Analysis")

    fig_acf, ax_acf = plt.subplots()
    plot_acf(close, ax=ax_acf, lags=40)
    st.pyplot(fig_acf)

    fig_pacf, ax_pacf = plt.subplots()
    plot_pacf(close, ax=ax_pacf, lags=40)
    st.pyplot(fig_pacf)

    # -----------------------
    # MODEL: AR (p,0,0)
    # -----------------------
    if model_choice == "AR":
        st.subheader("🔮 Auto Regression (AR)")

        p = st.slider("p (lags)", 1, 10, 2)

        model = ARIMA(close, order=(p, 0, 0))
        model_fit = model.fit()

        forecast = model_fit.forecast(steps=30)

    # -----------------------
    # MODEL: MA (0,0,q)
    # -----------------------
    elif model_choice == "MA":
        st.subheader("🔮 Moving Average Model (MA)")

        q = st.slider("q (lags)", 1, 10, 2)

        model = ARIMA(close, order=(0, 0, q))
        model_fit = model.fit()

        forecast = model_fit.forecast(steps=30)

    # -----------------------
    # MODEL: ARMA (p,0,q)
    # -----------------------
    elif model_choice == "ARMA":
        st.subheader("🔮 ARMA Model")

        p = st.slider("p", 1, 5, 2)
        q = st.slider("q", 1, 5, 2)

        model = ARIMA(close, order=(p, 0, q))
        model_fit = model.fit()

        forecast = model_fit.forecast(steps=30)

    # -----------------------
    # MODEL: ARIMA (p,d,q)
    # -----------------------
    elif model_choice == "ARIMA":
        st.subheader("🔮 ARIMA Model")

        p = st.slider("p", 1, 5, 2)
        d = st.slider("d", 0, 2, 1)
        q = st.slider("q", 1, 5, 2)

        model = ARIMA(close, order=(p, d, q))
        model_fit = model.fit()

        forecast = model_fit.forecast(steps=30)

    # -----------------------
    # Plot Forecast
    # -----------------------
    fig2, ax2 = plt.subplots()

    ax2.plot(close, label="Original")
    ax2.plot(range(len(close), len(close) + 30),
             forecast, linestyle="dashed", label="Forecast")

    ax2.legend()
    st.pyplot(fig2)

    st.subheader("📅 Next 30 Days Prediction")
    st.write(forecast)

else:
    st.warning("Invalid stock symbol or no data found")