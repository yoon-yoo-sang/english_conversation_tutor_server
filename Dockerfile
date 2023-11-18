FROM python:3.11-alpine AS builder
EXPOSE $PORT
ENV SECRET_KEY "dummy secret key"
WORKDIR /app
COPY requirements.txt /app
RUN pip3 install -r requirements.txt
COPY . /app
RUN python3 manage.py migrate users
RUN python3 manage.py migrate
CMD ["sh", "-c", "echo Port is $PORT && exec gunicorn config.wsgi:application --bind 0.0.0.0:$PORT"]

