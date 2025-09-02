from airflow.providers.docker.operators.docker import DockerOperator
from docker.types import Mount
from datetime import datetime
from pendulum import timezone # Assuming you use pendulum for timezone-aware dates

# Define the host paths
HOST_PROJECTS_PATH = '/home/carenk/my_data/01_projects/04_isra/01_etl_result'
HOST_DATA_PATH = '/home/carenk/my_data/01_projects/04_isra/02_fastapi/mnt/images'

# Define the container paths
CONTAINER_PROJECTS_PATH = '/app/projects'
CONTAINER_DATA_PATH = '/data_mounts'

beijing_tz = timezone('Asia/Shanghai')

with DAG(
    dag_id='etl_isra_report_etl_main',
    # Ensure start_date is timezone-aware
    start_date=datetime(2025, 9, 1, 0, 0, tzinfo=beijing_tz),
    schedule_interval='*/30 * * * *',
    catchup=False,
    tags=['etl', 'isra'],
) as dag:
    run_etl_script = DockerOperator(
        task_id='execute_etl_isra_main',
        image='python_env_common:202507',
        command='bash -c "cd ' + CONTAINER_PROJECTS_PATH + ' && python etl_main.py"',
        mounts=[
            # Mount the project directory from the host into the container.
            Mount(source=HOST_PROJECTS_PATH, target=CONTAINER_PROJECTS_PATH, type='bind'),
            
            # Mount the data directory from the host into the container.
            Mount(source=HOST_DATA_PATH, target=CONTAINER_DATA_PATH, type='bind'),
        ],
        network_mode='network_docker_common_nginxuse',
        auto_remove=True,
    )
