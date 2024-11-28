from airflow import DAG
from airflow.providers.amazon.aws.hooks.s3 import S3Hook
from airflow.operators.python import PythonOperator
from datetime import datetime

#commen
def test_minio_connection():
    hook = S3Hook(aws_conn_id="minio")  # Replace with your Airflow connection ID
    buckets = hook.list_buckets()
    print(f"Successfully connected to MinIO. Buckets: {buckets}")

with DAG(
    dag_id="test_minio_connection",
    start_date=datetime(2023, 1, 1),
    schedule_interval=None,
    catchup=False,
) as dag:
    test_connection_task = PythonOperator(
        task_id="test_minio_connection",
        python_callable=test_minio_connection,
    )
