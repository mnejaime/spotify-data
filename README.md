# Spotify Top Tracks Data Pipeline

Figured a fun way to learn about some data science tools would be to look into my music listening habits!

This tool automates the collection of Spotify data and shows it in a dashboard. The goal of this project is not completeness of the dashboard, but for me to learn how to integrate the necessary technologies to make it work. Future enhancements include getting more data from the Spotify API and making real insights on the streamlit dashboard!

## What It Does

The pipeline does two main things:

- Automatically pulls your top tracks from Spotify's API and stores them in a PostgreSQL database using Airflow
- Shows your listening trends in a Streamlit dashboard that updates itself

I containerized everything with Docker so that setup is easy.

## Requirements

- Docker and Docker Compose

I ended up downloading the Docker desktop application, which makes it very easy to visualize and control your containers.
<https://www.docker.com/products/docker-desktop/>

- A Spotify Developer account (which is free)
<https://developer.spotify.com/dashboard>

## Getting Started

Create a `.env` file with your credentials. It should look like this:

```.env
# Database Credentials
DB_USER=your_username
DB_PW=your_password
DB_HOST=postgres
DB_PORT=5432
DB_NAME=mydb

# Your Spotify API credentials
SPOTIPY_CLIENT_ID=your_spotify_client_id
SPOTIPY_CLIENT_SECRET=your_spotify_client_secret
SPOTIPY_REDIRECT_URI=your_redirect_uri
```

I set my redirect URL to `http://localhost:1234/`

Then run:

```bash
docker-compose up --build
```

## Component Details

### Database

- PostgreSQL database storing top tracks information
- Automatically initialized with needed tables
- Data persisted using Docker volumes

### ETL Pipeline

- Located in `scripts/spotify_etl.py`
- Fetches top 50 tracks from your Spotify account
- Processes and stores track and artist information

### Airflow DAG

- Located in `dags/airflow_dag.py`
- Runs daily to refresh data
- Two-step pipeline: database setup → data extraction
- Accessible via Airflow UI at `http://localhost:8080`

### Dashboard

- Built with Streamlit
- Displays top artists and list of top tracks
- Accessible at `http://localhost:8501`

## Project Structure

```text
.
├── dags/
│   └── airflow_dag.py          # Airflow DAG definition
├── dashboard/
│   ├── dashboard_requirements.txt
│   ├── dockerfile              # Streamlit container setup
│   └── spotify_dashboard.py    # Dashboard implementation
├── docker-compose.yaml         # Main container orchestration
├── dockerfile                  # Airflow container setup
├── README.md
└── scripts/
    ├── database_setup.py       # Database initialization
    └── spotify_etl.py          # Spotify data extraction
```

## Usage

1. Go to `http://localhost:8080` to monitor the data pipeline
2. Look at your spotify metrics at `http://localhost:8501`

The data refreshes daily as long as the containers are running, but you can also trigger a manual refresh through Airflow.

## Troubleshooting

- Run `docker-compose ps` to make sure all containers are actually running
- Check Airflow logs
- Ensure database connection through streamlit dashboard
- Check Spotify API credentials if you're not getting any data

## Notes

- The pipeline uses Spotify's "user-top-read" scope
- Data is replaced daily to maintain current listening trends
- Dashboard updates automatically when new data is available
