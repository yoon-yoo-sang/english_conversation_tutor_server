FROM python:3.11-alpine AS dev
ARG SECRET_KEY
WORKDIR /app
COPY requirements.txt /app
RUN pip3 install -r requirements.txt
COPY . /app
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

FROM python:3.11-alpine AS prod
EXPOSE $PORT
# DUMMY SECRET KEY TO BE REPLACED BY HEROKU ENVIRONMENT VARIABLE
ENV SECRET_KEY="6b1e7b2c40930eca39fc6b96aec6a43f7c8e2c61c52d44f753"
WORKDIR /app
COPY requirements.txt /app
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
COPY . /app
CMD ["sh", "-c", "echo Port is $PORT && exec gunicorn config.wsgi:application --bind 0.0.0.0:$PORT"]