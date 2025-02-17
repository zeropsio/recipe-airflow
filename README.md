# Zerops x Apache Airflow

[Apache Airflow](https://airflow.apache.org/) is an open-source platform for orchestrating and scheduling complex data pipelines. It allows you to programmatically author, schedule, and monitor workflows as Directed Acyclic Graphs (DAGs).

![airflow](https://github.com/zeropsio/recipe-shared-assets/blob/main/covers/svg/cover-airflow.svg)

<br />


## Deploy on Zerops
Manually copy the [import yaml](https://github.com/zeropsio/recipe-airflow/blob/main/zerops-project-import.yml) to the import dialog in the Zerops app.

```yaml
project:
  name: Apache Airflow Standalone
  tags:
    - zerops-recipe
    - development
services:
  - hostname: airflowstandalone
    type: python@3.12
    verticalAutoscaling:
      minRam: 1
    maxContainers: 1
    buildFromGit: https://github.com/zeropsio/recipe-airflow
    enableSubdomainAccess: true
```

For production-ready, high-available setup use [production import yaml](https://github.com/zeropsio/recipe-airflow/blob/main/zerops-project-production-import.yml).

# Recipe Features
- Apache Airflow version `2.10`
- Python version `3.12`
- Showcase DAG file

## Development (Standalone)
- Standalone mode ([docs](https://airflow.apache.org/docs/apache-airflow/stable/start.html)), not recommended for production usage
- Access details can be found in runtime log, look for logs as the following:
```text
standalone | Airflow is ready
standalone | Login with username: admin  password: *****
standalone | Airflow Standalone is for development purposes only. Do not use this in production!
```

## Production
- Data are stored in Postgres
- Celery executor (running on redis)
- DAG files are distributed via shared storage (shared mounted volume)
- Only push to the `airflowdags` service to update your DAG files (either via `zcli push airflowdags` or connect your Git with the `airflowdags` service), other services will use the files located in the mounted volume
- UI access:
  - Username: `admin`
  - Password: `$ADMIN_PASSWORD` generated project environment variable (visible in GUI)

### Ways To Reduce Cost
- Change worker count
- Decrease scaling resources to minimum
- Change database services mode to `NON_HA` (historical data can be lost)

<br/>
<br/>

Need help setting your project up? Join [Zerops Discord community](https://discord.com/invite/WDvCZ54).