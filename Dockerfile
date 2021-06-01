FROM python:3.6-slim-buster
FROM tensorflow/tensorflow:2.5.0

RUN python -m pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /app
WORKDIR /app/app_files
ENV FLASK_APP=main

CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0"]