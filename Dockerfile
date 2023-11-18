FROM python:3.11-alpine AS builder
EXPOSE 8000
WORKDIR /app
COPY requirements.txt /app
RUN pip3 install -r requirements.txt
COPY . /app
ENTRYPOINT ["python3"]
CMD ["manage.py", "migrate", "users"]
CMD ["manage.py", "migrate", "chats"]
CMD ["manage.py", "migrate"]
CMD ["manage.py", "runserver", "0.0.0.0:8000"]