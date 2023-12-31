import numpy as np
import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

PAGE_CONFIG = {"page_title": "Currency Trend Prediction",
               "page_icon": "icon.jpg", "layout": "centered"}
st.set_page_config(**PAGE_CONFIG)

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://media.istockphoto.com/id/1156644488/vector/widescreen-abstract-financial-chart-with-uptrend-line-graph-and-candlestick-on-black-and.jpg?s=612x612&w=0&k=20&c=Zu295XMgPJ3RKhcfpUzezMZUComEqM5Q9N_C5X_m0NI=");
background-size: cover;
background-position: top left;
background-repeat: no-repeat;
}}
[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>EUR/INR Trend Prediction</h1>", unsafe_allow_html=True)

st.write(' ')
st.write(' ')

st.markdown('*Step into a world of currency prediction with the Euro to INR Currency Prediction App! This project is centered around the exploration and analysis of historical data to forecast future trends in the Euro to Indian Rupee (INR) exchange rates. Leveraging machine learning, specifically a Random Forest Regressor, the application uses a dataset comprising daily open, high, low, and volume values. Through meticulous data exploration, preprocessing, and model training, the project aims to deliver a tool that provides users with valuable insights for anticipating potential movements in the Euro to INR exchange rate. The significance of this project lies in its potential to equip users with data-driven perspectives, facilitating more informed decision-making in the ever-evolving landscape of currency trading.*')

st.write(' ')
st.write(' ')

st.markdown("<h4>Enter values:</h4>", unsafe_allow_html=True)

input_open = st.text_input('Open')
input_high = st.text_input('High')
input_low = st.text_input('Low')
input_change = st.text_input('Change %')

# data analysis
df = pd.read_csv('EUR_INR_data.csv')
df.drop(['Date'], axis=1, inplace=True)
df.drop(['Vol.'], axis=1, inplace=True)
df['Change %'] = df['Change %'].str.replace('%', '').astype(float)
features = ['Open', 'High', 'Low', 'Change %']
X = df[features]
y = df['Price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
model = RandomForestRegressor(random_state=42)
model.fit(X_train_scaled, y_train)

# model = joblib.load(r'currency_prediction_model.pkl')

if st.button('Submit'): 

    if input_open != '' and input_high != '' and input_low != '' and input_change != '':

        new_input = np.array([[int(input_open), int(input_high), int(input_low), int(input_change)]])
        # scaler = joblib.load(r'scaler.pkl')
        new_input_scaled = scaler.transform(new_input)

        predicted_price = model.predict(new_input_scaled)

        st.markdown("<h4>Predicted price:</h4>", unsafe_allow_html=True)

        st.success(str(round(predicted_price[0], 2)) + ' EUR')
    
    else:

        st.error('Enter all values.')
