FROM apache/airflow:2.8.1-python3.11

USER root
RUN pip install --no-cache-dir --upgrade pip

USER airflow
COPY ./dags /opt/airflow/dags