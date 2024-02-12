import json
from django import http
from django.urls import path
from django.db import transaction
from django.db import models

from django.core.exceptions import ValidationError

from django.apps import AppConfig


class MessagesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'messages'

class Message(models.Model):
    requester = models.TextField()
    message = models.TextField()

    def __str__(self):
        return f"Message {self.id} by {self.requester}"
    
    class Meta:
        db_table = "messages"



async def createMessage(request: http.HttpRequest) -> http.HttpResponse:
    try:
        parsed_input = json.loads(request.body)
    except json.JSONDecodeError:
        raise ValidationError('invalid json body')
    
    requester = parsed_input.get("requester", "default requester")
    message = parsed_input.get("message", "default message")
    result = await create_message(requester, message)

    return http.JsonResponse({"id": result.id})

async def create_message(requester: str, message: str) -> Message:
    new_message = Message(requester=requester, message=message)

    await new_message.asave()

    return new_message

app_name = "messages"
urlpatterns = [
    path("message", createMessage, name="create-message"),
]
