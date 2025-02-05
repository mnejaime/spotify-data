import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv('.env') # load our .env file

# get necessary information from .env, load into constants
USER = os.getenv("DB_USER")
PASSWORD = os.getenv("DB_PW")
HOST = os.getenv("DB_HOST") 
PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")


db_url = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"
engine = create_engine(db_url) # sqlalchemy creates a connection to the db

# Load data
df = pd.read_sql("SELECT * FROM top_spotify_tracks", engine)

# Dashboard UI
st.title("Spotify Listening Insights")
st.write("Take a look at what I listen to!")

st.subheader("Top Artists")
st.bar_chart(df['artist'].value_counts())

st.subheader("Top Songs and Artists")
st.dataframe(df)

# Run using `streamlit run spotify_dashboard.py`