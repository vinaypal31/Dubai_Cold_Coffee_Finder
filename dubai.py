import streamlit as st
import pandas as pd
from datetime import datetime
from geopy.distance import geodesic

st.title("☕︎ Dubai Cold Coffee Finder")

st.subheader("Nearest Coffee Spots")

dff = pd.read_csv("dubai_cold_coffee_spots_clean.csv")

def is_open(row):
    opening_time = row["opening_time"]
    closing_time = row["closing_time"]

    current_time = datetime.now().strftime("%H:%M")

    return opening_time <= current_time <= closing_time

with st.sidebar:
    st.title("Search Filters")
    st.subheader("Find Best Coffee Spot")

    user_lat = st.number_input("Enter Latitude :" ,25.20)
    user_lang = st.number_input("Enter Langitude :", 55.29)

    spot_type = st.selectbox("Select Spot Type" , ["All" , "Cart" , "Cafe" , "Truck"])

    is_open_spot = st.checkbox("Is Open", True)

    max_dis = st.slider("Max Distance" , 1, 15, 4)

dff["is_open"] = dff.apply(is_open, axis=1)

def calculate_distance(row):
    lat = row["lat"]
    lng = row["lng"]
    user = (user_lat , user_lang)
    distance = round(geodesic(user,(lat, lng)).km,2)
    return distance

dff["distance"] = dff.apply(calculate_distance, axis=1)



if spot_type == "All":
    dff = dff
else:
    dff = dff[dff["type"] == spot_type.lower()] 


if is_open_spot:
    dff = dff[dff["is_open"] == True]

dff = dff[dff["distance"] <= max_dis]
dff = dff.sort_values(by="distance", ignore_index=True)

st.dataframe(dff)

