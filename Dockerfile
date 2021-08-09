FROM python:3.8-slim-buster

WORKDIR /src

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY app app

CMD ["gunicorn", "app.main:app", "-w" ,"2", "-k", "uvicorn.workers.UvicornWorker", "-b", "0.0.0.0:5555"]
