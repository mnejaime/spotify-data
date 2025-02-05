import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
import plotly.express as px
import plotly.graph_objects as go

load_dotenv('.env') # load our .env file

# get necessary information from .env, load into constants
USER = os.getenv("DB_USER")
PASSWORD = os.getenv("DB_PW")
HOST = os.getenv("DB_HOST") 
PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")


db_url = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"
engine = create_engine(db_url) # sqlalchemy creates a connection to the db

# load data
df = pd.read_sql("SELECT * FROM top_spotify_tracks", engine)

# title and description
st.title("🎵 My Spotify Listening Analysis")
st.markdown("A look into my music preferences based on top tracks.")

# make a few columns for metrics
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Tracks", len(df))
    
with col2:
    st.metric("Unique Artists", df['artist'].nunique())
    
with col3:
    top_artist = df['artist'].mode()[0]
    st.metric("Most Featured Artist", top_artist)

# top artists
st.subheader("🎸 Top Artists Distribution")
fig_artists = px.bar(
    df['artist'].value_counts().reset_index(),
    x='artist',
    y='count',
    title="Number of Tracks per Artist",
    labels={'count': 'Number of Tracks', 'artist': 'Artist'},
)
fig_artists.update_layout(showlegend=False)
st.plotly_chart(fig_artists, use_container_width=True)

# track list
st.subheader("📝 Detailed Track List")
st.dataframe(
    df,
    column_config={
        "track": "Track Name",
        "artist": "Artist",
    },
    use_container_width=True
)

# footer with timestamp
st.markdown("---")
st.markdown("*Last updated: {}*".format(pd.Timestamp.now().strftime("%Y-%m-%d %H:%M:%S")))