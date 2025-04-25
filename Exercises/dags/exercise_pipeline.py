from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'exercise_pipeline',
    default_args=default_args,
    description='Pipeline chạy các bài tập từ 1-5',
    schedule_interval=timedelta(days=1),
    catchup=False
)

# Task cho Exercise 1
exercise_1 = BashOperator(
    task_id='exercise_1',
    bash_command='python /opt/airflow/dags/Exercise-1/main.py',
    dag=dag,
)

# Task cho Exercise 2
exercise_2 = BashOperator(
    task_id='exercise_2',
    bash_command='python /opt/airflow/dags/Exercise-2/main.py',
    dag=dag,
)

# Task cho Exercise 3
exercise_3 = BashOperator(
    task_id='exercise_3',
    bash_command='python /opt/airflow/dags/Exercise-3/main.py',
    dag=dag,
)

# Task cho Exercise 4
exercise_4 = BashOperator(
    task_id='exercise_4',
    bash_command='python /opt/airflow/dags/Exercise-4/main.py',
    dag=dag,
)

# Task cho Exercise 5
exercise_5 = BashOperator(
    task_id='exercise_5',
    bash_command='python /opt/airflow/dags/Exercise-5/main.py',
    dag=dag,
)

# Thiết lập thứ tự chạy các task
exercise_1 >> exercise_2 >> exercise_3 >> exercise_4 >> exercise_5 