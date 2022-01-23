FROM python:3.9.1

RUN apt-get install wget
RUN pip install pandas 
RUN pip install sqlalchemy 
RUN pip install psycopg2

WORKDIR /app
COPY ingest_file.py ingest_file.py 

ENTRYPOINT [ "python", "ingest_file.py" ]