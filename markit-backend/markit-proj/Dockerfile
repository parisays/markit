FROM python:3.7
ENV PYTHONUNBUFFERED 1
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN mkdir /code
WORKDIR /code
COPY . /code/
ENV POSTGRES_USER markit
ENV POSTGRES_PASSWORD sebackendfall19
ENV POSTGRES_DB markitdb
