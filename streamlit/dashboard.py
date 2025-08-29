import streamlit as st
import requests # pyright: ignore[reportMissingModuleSource]

API_URL = "http://api:8000"  # internal Docker name

st.title("📈 Risk Dashboard")

portfolio_name = st.text_input("Portfolio Name", "Tech Stocks")
tickers_raw = st.text_area("Enter tickers and weights (e.g. AAPL:0.3, MSFT:0.7)", "AAPL:0.5, MSFT:0.5")

if st.button("Calculate Risk"):
    try:
        tickers = [{"ticker": t.split(":")[0].strip(), "weight": float(t.split(":")[1])} for t in tickers_raw.split(",")]
        payload = {
            "portfolio_name": portfolio_name,
            "tickers": tickers
        }
        response = requests.post(f"{API_URL}/portfolio", json=payload)
        if response.status_code == 200:
            data = response.json()
            st.success(f"✅ Results for: {data['portfolio_name']}")
            st.metric("VaR 95%", f"${data['var_95']:.2f}")
            st.metric("VaR 99%", f"${data['var_99']:.2f}")
            st.metric("Stress Loss", f"${data['stress_loss']:.2f}")
            st.download_button("Download CSV", data=response.text, file_name="risk.csv", mime="text/csv")
        else:
            st.error("API Error: " + response.text)
    except Exception as e:
        st.error(f"⚠️ Invalid input: {e}")