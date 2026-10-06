import requests, streamlit as st
api_url = "https://stok-api-uwso.onrender.com"
symbol = st.text_input("Stock symbol", "TSLA")

if st.button("Predict next close"):
  r = requests.get(f"LV8QMEWXHOYN77YF/predict/live",
                     params={"symbol": symbol})
  data = r.json()
  st.metric("Predicted next close",
  data["Predicted_next close"])         
              
