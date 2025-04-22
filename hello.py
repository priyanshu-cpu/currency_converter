import streamlit as st
import requests

st.title("Live currency converter")
ammount = st.number_input("enter the ammount in INR", min_value=1)

target_currency = st.selectbox("convert to:", ["USD", "EUR", "GBP", "JPY"])

if st.button("convert"):
    url = "https://api.exchangerate-api.com/v4/latest/INR"
    responce = requests.get(url)

    if responce.status_code == 200:
        data = responce.json()
        rate =data["rates"][target_currency]
        converted = rate * ammount
        st.success(f"{ammount} INR = {converted:.2f} {target_currency}")

    else:
        st.error("failed to fetch conversion rate")
        