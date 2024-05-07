from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.models import Variable
import requests

# Define the function to be executed by the PythonOperator
def fetch_data():
    # Retrieve the API key from Airflow variables
    api_key = Variable.get("my_api_key")

    # Make a request to the API using the API key
    response = requests.get(f"https://api.example.com/data?api_key={api_key}")

    # Process the response data (for simplicity, let's just print it)
    print(response.json())

# Define the DAG
with DAG('example_dag_using_variables', schedule_interval='@daily') as dag:
    # Define the PythonOperator
    fetch_data_task = PythonOperator(
        task_id='fetch_data_task',
        python_callable=fetch_data,
    )

    # Define the task dependencies
    fetch_data_task
