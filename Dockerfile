FROM python:3.11-alpine AS builder
WORKDIR /app
COPY requirements.txt /app
RUN pip3 install -r requirements.txt
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV SECRET_KEY="django"
COPY . /app
RUN python3 manage.py migrate users
RUN python3 manage.py migrate

EXPOSE $PORT
CMD ["python3", "manage.py", "runserver", "0.0.0.0:$PORT"]