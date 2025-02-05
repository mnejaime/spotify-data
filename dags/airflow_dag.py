from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
# Import existing functions
import sys
sys.path.append("/opt/airflow/scripts") # Ensure dag has access to scripts
from spotify_etl import get_spotify_data
from database_setup import make_db

default_args = {
    'owner': 'mike',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'start_date': datetime(2024, 2, 4)
}

with DAG(
    'spotify_pipeline',
    default_args=default_args,
    description='Pipeline for Spotify data',
    schedule_interval='@daily'
) as dag:

    setup_db = PythonOperator(
        task_id='setup_database',
        python_callable=make_db,
    )

    spotify_etl = PythonOperator(
        task_id='spotify_etl',
        python_callable=get_spotify_data
    )

    setup_db >> spotify_etl