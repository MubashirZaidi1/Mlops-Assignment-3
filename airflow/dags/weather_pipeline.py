from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG("weather_pipeline",
         start_date=datetime(2024, 1, 1),
         schedule_interval="@daily",
         catchup=False) as dag:

    fetch_data = BashOperator(
        task_id="fetch_data",
        bash_command="python3 /path/to/your/project/scripts/fetch_data.py"
    )

    preprocess = BashOperator(
        task_id="preprocess_data",
        bash_command="python3 /path/to/your/project/scripts/preprocess_data.py"
    )

    fetch_data >> preprocess
