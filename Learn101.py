import streamlit as st, pandas as pf, yfinance as yf
import plotly.express as px 

# Page title
st.set_page_config(page_title='Stock Dashboard', page_icon='📊')
st.title('📊 Stock Dashboard')
ticker = st.sidebar.text_input('Ticker')
start_date = st.sidebar.date_input('Start Date')
end_date = st.sidebar.date_input('End Date')


