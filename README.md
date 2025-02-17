# Zerops x Apache Airflow

Apache Airflow is an open-source platform for orchestrating and scheduling complex data pipelines. It allows you to programmatically author, schedule, and monitor workflows as Directed Acyclic Graphs (DAGs).

![airflow](https://github.com/zeropsio/recipe-shared-assets/blob/main/covers/svg/cover-airflow.svg)

<br />

# Install

- Apache Airflow version `2.10`
- Python version `3.12`

## Development (Standalone)
- Find out UI login access in runtime logs.

## Production
- Celery executor.
- DAG files are distributed via shared storage (shared mounted volume).
- Only push to the `airflowdags` service to update your DAG files (either via `zcli push airflowdags` or connect your Git with the `airflowdags` service), other services will use the files located in the mounted volume (using symbolic link to `$AIRFLOW_HOME/dags`).
- UI access:
  - Username: `admin`
  - Password: `$ADMIN_PASSWORD` project environment variable

### Ways To Reduce Cost
- Change worker count.
- Decrease scaling resources to minimum.
