from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

dag = DAG(
    'dvc_pipeline_stages',
    default_args=default_args,
    description='Run DVC pipeline stages independently',
    schedule_interval='@daily',
    catchup=False,
)

# Replace this with your full project path
project_dir = "/home/mubashir/Desktop/Assignment 3/weather_pipeline"
python_env = "source venv/bin/activate"

fetch = BashOperator(
    task_id='fetch_data',
    bash_command=f'cd "{project_dir}" && {python_env} && dvc repro fetch_data',
    dag=dag,
)

preprocess = BashOperator(
    task_id='preprocess_data',
    bash_command=f'cd "{project_dir}" && {python_env} && dvc repro preprocess_data',
    dag=dag,
)

train = BashOperator(
    task_id='train_model',
    bash_command=f'cd "{project_dir}" && {python_env} && dvc repro train_model',
    dag=dag,
)

fetch >> preprocess >> train
