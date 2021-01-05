from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(0,0,0,0,0),
    'email': ['tahak92@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 2,
    'retry_delay': timedelta(minutes=1),
}

dag = DAG(
    'first_dag',
    default_args=default_args,
    description='This is the first dag for this pipeline',
    schedule_interval=timedelta(days=1),
)

def just_a_function():
    print("This is a test")


run_etl = PythonOperator(
    task_id='first_task',
    python_callable=just_a_function,
    dag=dag
)

run_etl