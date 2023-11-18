# English Conversation Tutor Server
english conversation tutoring server with django and openai

python: 3.11.5

```
├── config/                 # Django main project directory
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── chats/                  # Chat application directory
│   ├── migrations/
│   │   └── __init__.py
│   ├── __init__.py
│   ├── admin.py 
│   ├── apps.py 
│   ├── models.py
│   ├── tests.py 
│   ├── views.py 
│   └── serializers.py 
├── users/                  # User application directory
│   ├── migrations/
│   │   └── __init__.py
│   ├── __init__.py
│   ├── admin.py 
│   ├── apps.py 
│   ├── models.py
│   ├── tests.py 
│   ├── views.py 
│   └── serializers.py 
│
├── openai_integration/     # OpenAI integration directory
│   ├── __init__.py
│   ├── tools.py
│   ├── openai_chat.py
│   └── choices.py
│
├── manage.py
├── .gitignore
├── manage.py
├── README.md
├── docker-compose.yaml
├── Dockerfile
└── requirements.txt
```
