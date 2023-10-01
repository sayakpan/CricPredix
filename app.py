import streamlit as st
import pandas as pd
import numpy as np
import pickle
from tabulate import tabulate

teams = [
    "Australia",
    "India",
    "Bangladesh",
    "New Zealand",
    "South Africa",
    "England",
    "West Indies",
    "Afghanistan",
    "Pakistan",
    "Sri Lanka",
]

cities = [
    "Colombo",
    "Mirpur",
    "Johannesburg",
    "Dubai",
    "Auckland",
    "Cape Town",
    "London",
    "Pallekele",
    "Barbados",
    "Sydney",
    "Melbourne",
    "Durban",
    "St Lucia",
    "Wellington",
    "Lauderhill",
    "Hamilton",
    "Centurion",
    "Manchester",
    "Abu Dhabi",
    "Mumbai",
    "Nottingham",
    "Southampton",
    "Mount Maunganui",
    "Chittagong",
    "Kolkata",
    "Lahore",
    "Delhi",
    "Nagpur",
    "Cardiff",
    "Chandigarh",
    "Adelaide",
    "Bangalore",
    "St Kitts",
    "Christchurch",
    "Trinidad",
]

pipe = pickle.load(open("pipe.pkl", "rb"))

st.markdown(
    "<h1 style='text-align: center;'>CricPredix</h1><h4 style='text-align: center;margin-bottom:1rem;'>T20 Cricket Score Predictor</h4>",
    unsafe_allow_html=True,
)

col1, col2, col3 = st.columns(3)

with col1:
    batting_team = st.selectbox("Select Batting Team", sorted(teams))

with col2:
    st.markdown(
        "<h2 style='pointer-events: none; text-align:center;'>Vs</h2>",
        unsafe_allow_html=True,
    )  # Center vertically

with col3:
    bowling_team = st.selectbox("Select Bowling Team", sorted(teams))

city = st.selectbox("Select City", sorted(cities))

st.write("---")

col3, col4, col5 = st.columns(3)

with col3:
    current_score = st.number_input("Current Score", step=1)

with col4:
    wickets = st.number_input("Wickets Fallen", max_value=10, step=1)

with col5:
    overs = st.number_input("Overs Played Already", min_value=5, max_value=20, step=1)

last_five = st.number_input("Runs scored in last 5 overs", step=1)

if last_five > current_score:
    st.error("Last 5 over score cannot be greater than current score !")


if st.button("Predict Score"):
    balls_left = 120 - (overs * 6)
    wickets_left = 10 - wickets
    crr = current_score / overs

    input_df = pd.DataFrame(
        {
            "batting_team": [batting_team],
            "bowling_team": [bowling_team],
            "city": [city],
            "current_score": [current_score],
            "balls_left": [balls_left],
            "wickets_left": [wickets_left],
            "crr": [crr],
            "last_five": [last_five],
        }
    )

    print(tabulate(input_df))
    result = pipe.predict(input_df)
    print(result)

    if current_score == 0:
        st.error("Please enter valid data")
    else:
        st.header("Predicted Score : " + str(int(result[0])))

st.text("Built by Sayak")
