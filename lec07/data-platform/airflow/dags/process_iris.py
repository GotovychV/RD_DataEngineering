from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.email import EmailOperator
from datetime import datetime
from dbt_operator import DbtOperator
from python_scripts.train_model import process_iris_data
import pytz
import os

PROJECT_DIR = os.getenv('AIRFLOW_HOME')+"/dags/dbt/homework"
GMT3_tz = pytz.timezone('Europe/Kiev')  # GMT+3 timezone for Kyiv

# 🔹 DAG
with DAG(
    dag_id="process_iris",
    start_date=datetime(2025, 4, 22, tzinfo=GMT3_tz),
    end_date=datetime(2025, 4, 24, tzinfo=GMT3_tz),    
    schedule_interval='0 1 * * *',
    catchup=False,
    tags=["ml", "iris", "dbt"]
) as dag:

    dbt_task = DbtOperator(
        task_id="run_dbt",
        profile="homework",
        project_dir=PROJECT_DIR,
        command="run"
    )

    train_task = PythonOperator(
        task_id="train_and_upload_model",
        python_callable=process_iris_data
    )

    notify_task = EmailOperator(
        task_id='notify_success',
        to='gotovych@gmail.com',
        subject='Airflow DAG process_iris успішно виконано',
        html_content='Всі таски в складі DAG process_iris виконані успішно!'
    )

dbt_task >> train_task >> notify_task