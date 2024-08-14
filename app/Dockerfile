FROM python:alpine3.20

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

ENV PORT=8090
ENV GUNICORN_CMD_ARGS="--workers 2 --threads 4 --bind :$PORT"

EXPOSE $PORT

ENTRYPOINT [ "gunicorn", "app:app" ]