from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.email import EmailOperator
import requests
import pickle
import os
from dbt_operator import DbtOperator

PROJECT_DIR = os.getenv('AIRFLOW_HOME')+"/dags/dbt/homework"
ANALYTICS_DB = os.getenv('ANALYTICS_DB', 'analytics')
PROFILE = 'homework'

# Environment variables to pass to dbt
env_vars = {
    'ANALYTICS_DB': ANALYTICS_DB,
    'DBT_PROFILE': PROFILE
}

# 🔹 2. Функція: Тренування ML-моделі
def train_model():
    pass

# 🔹 DAG
with DAG(
    dag_id="process_iris",
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False,
    tags=["ml", "iris", "dbt"]
) as dag:

    dbt_task_run = DbtOperator(
        task_id="run_dbt",
        profile="homework",
        project_dir=PROJECT_DIR,
        command="run",
        #env_vars=env_vars,
        #models=["staging", "mart"]
    )

'''
    dbt_task_seed = DbtOperator(
        task_id="seed_dbt",
        profile="homework",
        project_dir=PROJECT_DIR,
        command="seed",
        #env_vars=env_vars,
        #models=["staging", "mart"]
    )

    train_task = PythonOperator(
        task_id="train_and_upload_model",
        python_callable=train_model
    )

    notify = EmailOperator(
        task_id='notify_success',
        to='gotovych@gmail.com',
        subject='Airflow DAG process_iris успішно виконано',
        html_content='Всі таски DAG виконані успішно!'
    )
'''

#dbt_task_seed >> dbt_task_run
