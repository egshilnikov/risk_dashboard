from airflow import DAG
from airflow.operators.python import PythonOperator # pyright: ignore[reportMissingImports]
from datetime import datetime

def hello():
    print("👋 Hello from lightweight Airflow!")

with DAG("light_dag", start_date=datetime(2023, 1, 1), schedule_interval="@daily", catchup=False) as dag:
    PythonOperator(task_id="say_hello", python_callable=hello)