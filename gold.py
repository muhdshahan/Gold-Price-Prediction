import streamlit as st
import joblib
import numpy as np
import time

# Load the model
model = joblib.load('final_model.joblib')

# Static USD to INR conversion
usd_to_inr = 83.50

st.set_page_config(page_title="Gold Price Prediction", page_icon="💰", layout="centered")

st.title("💰 Gold Price Predictor")
st.subheader("Predict the price of Gold in USD and INR.")

with st.sidebar:
    st.header("📊 Input Features")
    spx = st.slider('S&P 500 Index (SPX)', min_value=-2.0, max_value=3.0, step=0.01)
    gld_lag1 = st.slider('GLD Price 1 Day Ago', min_value=70, max_value=190, step=1)
    uso = st.slider('Crude Oil ETF (USO)', min_value=-1.4, max_value=2.7, step=0.01)
    slv = st.slider('Silver ETF (SLV)', min_value=-1.7, max_value=2.2, step=0.01)
    eurusd = st.slider('EUR/USD Exchange Rate', min_value=1.0, max_value=1.6, step=0.01)

if spx < 0:
    st.warning("SPX has a negative value, which may represent unusual market conditions.")
if slv < 0:
    st.warning("SLV has a negative value, which may represent unusual market conditions.")

# Main Input section
st.markdown("### 📥 Enter the features to predict the price:")
spx = st.number_input('S&P 500 Index (SPX)', format="%.4f", value=spx)
gld_lag1 = st.number_input('GLD Price 1 Day Ago', format="%.4f", value=gld_lag1)
uso = st.number_input('Crude Oil ETF (USO)', format="%.4f", value=uso)
slv = st.number_input('Silver ETF (SLV)', format="%.4f", value=slv)
eurusd = st.number_input('EUR/USD Exchange Rate', format="%.4f", value=eurusd)

# Predict button
if st.button('🎯 Predict GLD Price'):
    with st.spinner("Running prediction..."):
        time.sleep(2)
        
        input_data = np.array([[spx, gld_lag1, uso, slv, eurusd]])
        prediction_usd = model.predict(input_data)[0]
        prediction_inr = prediction_usd * usd_to_inr

    st.balloons() 

    # Show the result
    st.success("✅ Prediction Complete!")
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="💵 GLD Price (USD)", value=f"${prediction_usd:.2f}")
    with col2:
        st.metric(label="🇮🇳 GLD Price (INR)", value=f"₹{prediction_inr:.2f}")

