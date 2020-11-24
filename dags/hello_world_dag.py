from datetime import datetime

# Import DAG object
from airflow import DAG

# Import Python Operator we will use
from airflow.operators.python_operator import PythonOperator


def say_hello(name):
    words = "Hello " + name + "!"
    print(words)
    return words


# Create a DAG object with configuration
dag = DAG('hello_dag',
          description='Hello World DAG',
          start_date=datetime(2020, 11, 10),
          catchup=False)

# Create a Task
task1 = PythonOperator(
    task_id='hello_world_task',
    python_callable=say_hello,
    # Pass arguments to the python method
    op_kwargs={'name': 'World'},
    dag=dag)

# Create another Task
task2 = PythonOperator(
    task_id='hello_airflow_task',
    python_callable=say_hello,
    # Pass the value from Variable to the python method
    op_kwargs={'name': "Airflow"},
    dag=dag)

# Define the order of tasks
task1 >> [task2]
