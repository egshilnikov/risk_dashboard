FROM python:3.11-slim

ENV AIRFLOW_HOME=/opt/airflow

RUN apt-get update && apt-get install -y build-essential libpq-dev curl \
 && pip install --no-cache-dir apache-airflow==2.8.1 --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.8.1/constraints-3.11.txt" \
 && apt-get remove -y build-essential libpq-dev curl \
 && apt-get autoremove -y && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

RUN mkdir -p $AIRFLOW_HOME/dags

WORKDIR $AIRFLOW_HOME
COPY ./dags ./dags
COPY airflow.cfg .

CMD ["airflow", "webserver"]