
FROM python:3.9

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt --no-cache-dir

ENV CONTAINER_DB_HOST=db

CMD ["python", "/app/collect_weather.py"]