import streamlit as st
from used_car_price_estimation import show_used_car_price_estimation_page
from CO2_emission_estimation import show_CO2_emission_estimation_page

page = st.sidebar.selectbox("Used Car Price or CO2 Emission Estimation",("Used Car Price Estimation","CO2 Emission Estimation"))

if page == "Used Car Price Estimation":
    show_used_car_price_estimation_page()
else:
    show_CO2_emission_estimation_page()

