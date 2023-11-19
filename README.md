# English Conversation Tutor Server
English conversation tutoring server with Django and Openai. Pack in Docker and use Heroku by cloud platform.

python version: 3.11.5

```
├── .github/                # Github action deploy configure
│   └── workflows/
│       └── deploy.yml
│
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
├── .gitignore
├── Dockerfile
├── Procfile
├── README.md
├── docker-compose.yaml
├── heroku.yml
├── manage.py
├── requirements.txt
└── runtime.txt
```
