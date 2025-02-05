import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.sql import text

load_dotenv('.env') # load our .env file

# get necessary information from .env, load into constants
USER = os.getenv("DB_USER")
PASSWORD = os.getenv("DB_PW")
HOST = os.getenv("DB_HOST") 
PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")


db_url = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"
engine = create_engine(db_url) # sqlalchemy creates a connection to the db

def make_db():
    """ makes me tables in the DB if they don't exist! """
    with engine.connect() as connection: # engine.connect() will open and close bc of python with
        connection.execute(text("""
                       CREATE TABLE IF NOT EXISTS top_spotify_tracks(
                           id SERIAL PRIMARY KEY,
                           track_name TEXT,
                           artist TEXT
                        );
                        """))
    print("made u a table successfully!")

if __name__ == "__main__":
    make_db()