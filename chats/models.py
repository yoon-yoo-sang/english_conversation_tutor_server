from django.db import models


class OpenAIModel(models.TextChoices):
    NEW_GPT4 = "gpt-4-1106-preview"
    GPT4 = "gpt-4"
    GPT3 = "gpt-3.5-turbo-1106"
