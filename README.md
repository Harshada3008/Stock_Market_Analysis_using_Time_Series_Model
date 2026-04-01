<img width="1917" height="1014" alt="Screenshot 2026-04-01 102641" src="https://github.com/user-attachments/assets/4ef1452a-22db-418b-9609-b375ceee216f" />
<img width="1909" height="968" alt="Screenshot 2026-04-01 102714" src="https://github.com/user-attachments/assets/cef05240-cd3f-4c92-b72f-0634698a7a93" />
<img width="1747" height="845" alt="Screenshot 2026-04-01 102733" src="https://github.com/user-attachments/assets/7326b114-5466-49ab-be81-cfb117716403" />
<img width="1730" height="1008" alt="Screenshot 2026-04-01 102750" src="https://github.com/user-attachments/assets/5452a02f-742f-43bf-a76d-1f24296f3618" />
<img width="1655" height="921" alt="Screenshot 2026-04-01 102804" src="https://github.com/user-attachments/assets/bf505b9e-8f5b-4c85-b685-178c5c46fe4c" />
<img width="1678" height="894" alt="Screenshot 2026-04-01 102833" src="https://github.com/user-attachments/assets/2e5873cc-1f34-4a47-b5cd-f8416204f9f3" />


# 📈 Stock Market Prediction using Time Series Models

This project is a **Streamlit-based web application** that performs stock market analysis and forecasting using classical time series models:

- AR (Auto Regression)
- MA (Moving Average)
- ARMA (Auto Regressive Moving Average)
- ARIMA (Auto Regressive Integrated Moving Average)

It also includes **ACF (AutoCorrelation Function)** and **PACF (Partial AutoCorrelation Function)** plots to help in model selection.

---

## 🚀 Features

✅ Fetch real-time stock data using Yahoo Finance  
✅ Interactive UI built with Streamlit  
✅ Visualize stock closing prices  
✅ ACF & PACF analysis  
✅ Select and apply different time-series models  
✅ Predict next 30 days stock prices  
✅ Dynamic parameter tuning (p, d, q)

---

## 🛠️ Tech Stack

- Python 🐍  
- :contentReference[oaicite:0]{index=0}  
- :contentReference[oaicite:1]{index=1} API via yfinance  
- Statsmodels  
- Pandas & NumPy  
- Matplotlib  

---
## 📊 Models Used
🔹 AR (Auto Regression)

Uses past values to predict future values.

🔹 MA (Moving Average)

Uses past forecast errors.

🔹 ARMA

Combination of AR and MA.

🔹 ARIMA

Handles non-stationary data using differencing.
## 📉 ACF & PACF
ACF → Helps identify MA(q)
PACF → Helps identify AR(p)

These plots are used for selecting optimal model parameters.
## 📅 Output
Stock price visualization
ACF & PACF graphs
Forecast plot for next 30 days
Numerical prediction values
