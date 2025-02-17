from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
import random


def task_1_function():
    # Generate a random number and pass it to the next task.
    random_value = random.randint(1, 100)
    print(f"Generated random value: {random_value}")
    return random_value  # This will be automatically pushed to XCom.


def task_2_function(ti):
    # Pull the value from the previous task.
    received_value = ti.xcom_pull(task_ids='task_1')
    print(f"Received value from task 1: {received_value}")
    print(f"Double the value: {received_value * 2}")


with DAG(
        'simple_showcase_dag',
        description='A simple showcase DAG with two dependent tasks.',
        schedule_interval='* * * * *',  # Cron expression for every minute.
        start_date=datetime(2024, 6, 20),  # Set to past date for immediate availability.
        catchup=False  # Don't run for past dates.
) as dag:
    task_1 = PythonOperator(
        task_id='task_1',
        python_callable=task_1_function
    )

    task_2 = PythonOperator(
        task_id='task_2',
        python_callable=task_2_function
    )

    task_1 >> task_2  # This means task_2 depends on task_1.
