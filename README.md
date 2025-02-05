# Spotify Top Tracks Data Pipeline

A containerized data pipeline that automatically fetches your Spotify listening history and visualizes it through a Streamlit dashboard. The pipeline uses Airflow for orchestration, PostgreSQL for data storage, and Docker for containerization.

## Project Overview

This project consists of three main components:

1. An ETL pipeline that fetches top tracks data from Spotify's API
2. An Apache Airflow workflow that automates the data collection process
3. A Streamlit dashboard that visualizes your listening habits

## Prerequisites

- Docker and Docker Compose
- Spotify Developer Account (for API credentials)
- Python 3.x

## Setup Instructions

1. **Environment Variables**

Create a `.env` file in the root directory with the following variables:

```.env
# Database Configuration
DB_USER=your_username
DB_PW=your_password
DB_HOST=postgres
DB_PORT=5432
DB_NAME=mydb

# Spotify API Credentials
SPOTIPY_CLIENT_ID=your_spotify_client_id
SPOTIPY_CLIENT_SECRET=your_spotify_client_secret
SPOTIPY_REDIRECT_URI=your_redirect_uri
```

2. **Start the Services**

```bash
docker-compose up --build
```

This will start:

- PostgreSQL database (port 5432)
- Airflow webserver (port 8080)
- Streamlit dashboard (port 8501)

## Component Details

### Database

- PostgreSQL database storing top tracks information
- Automatically initialized with required tables
- Data persisted using Docker volumes

### ETL Pipeline

- Located in `scripts/spotify_etl.py`
- Fetches top 50 tracks from authenticated user's Spotify account
- Processes and stores track and artist information

### Airflow DAG

- Located in `dags/airflow_dag.py`
- Runs daily to refresh data
- Two-step pipeline: database setup → data extraction
- Accessible via Airflow UI at `http://localhost:8080`

### Dashboard

- Built with Streamlit
- Displays top artists bar chart
- Shows complete list of top tracks
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

1. Access Airflow UI at `http://localhost:8080` to monitor pipeline runs
2. View your Spotify insights at `http://localhost:8501`
3. Data automatically refreshes daily through the Airflow pipeline

## Development

To modify the pipeline:

1. Update ETL logic in `scripts/spotify_etl.py`
2. Modify dashboard visualizations in `dashboard/spotify_dashboard.py`
3. Adjust DAG schedule in `dags/airflow_dag.py`

## Troubleshooting

- Ensure all containers are running: `docker-compose ps`
- Check Airflow logs for pipeline issues
- Verify database connection through the Streamlit dashboard
- Ensure Spotify API credentials are correctly configured

## Notes

- The pipeline uses Spotify's "user-top-read" scope
- Data is replaced daily to maintain current listening trends
- Dashboard updates automatically when new data is available
