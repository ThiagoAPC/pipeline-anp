from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import os

def extract():
    os.system("python /usr/local/airflow/dags/scripts/extract_anp.py")

def transform():
    os.system("python /usr/local/airflow/dags/scripts/transform_anp.py")

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 1),
    'retries': 1
}
dag = DAG('pipeline_preco_produtos', default_args=default_args, schedule_interval='@weekly')
extract_task = PythonOperator(task_id='extract_data', python_callable=extract, dag=dag)
transform_task = PythonOperator(task_id='transform_data', python_callable=transform, dag=dag)
extract_task >> transform_task