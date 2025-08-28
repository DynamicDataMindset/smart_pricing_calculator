#import libraries
import streamlit as st
import yfinance as yf

#function to fetch usd/zar exchange rate
def get_usd_to_zar():
    ticker = yf.Ticker("ZAR=X")
    data = ticker.history(period="1d")
    latest_rate = data["Close"].iloc[-1]
    return latest_rate

# Streamlit UI
st.title("💰 Msquared Price Calculator")

usd_price = st.number_input("Enter Product Price in USD:", min_value=0.0, value=1000.0)

if st.button("Calculate"):
    usd_zar = get_usd_to_zar()
    adjusted_rate = usd_zar + 1.50
    base_price_zar = usd_price * adjusted_rate
    excl_vat = base_price_zar * 1.35
    incl_vat = excl_vat * 1.15

    st.write(f"💵 Current exchange rate → {usd_zar:.2f}")
    st.write(f"📉 Exchange rate used → {adjusted_rate:.2f}")
    st.success(f"💰 Excluding VAT → R{excl_vat:,.2f}")
    st.success(f"💰 Including VAT → R{incl_vat:,.2f}")