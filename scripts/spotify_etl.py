# This file will grab data from the Spotipy API, and load it into a PostgreSQL database

import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv
import pandas as pd
from database_setup import engine

load_dotenv('.env') # load my .env file that has my darkest secrets (OAuth credentials)

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=os.getenv("SPOTIPY_CLIENT_ID"),
                                               client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
                                               redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
                                               scope="user-top-read"))


def get_spotify_data():
    
    top_tracks = sp.current_user_top_tracks(limit=50) # grab my user's top 50 tracks
    
    cleaned_dict_of_tracks = [] # new dictionary to get only the information I want (track and artist)
    
    for item in top_tracks['items']: # iterate over top_tracks to grab relevant data and append to cleaned_dict_of_tracks
        cleaned_dict_of_tracks.append({
            'track': item['name'],
            'artist': item['artists'][0]['name']
        })

    df = pd.DataFrame.from_dict(cleaned_dict_of_tracks) # turn into pandas dataframe
    df.to_sql('top_spotify_tracks', engine, if_exists='replace', index=False) 
    # and turn into sql, we'll replace the table if data is already there. 
    # index not needed, bc already in the sql database that we set up
    
    
if __name__ == "__main__":
    get_spotify_data()