# myapp/urls.py
from django.urls import path
from .views import chat

app_name = 'myapp'

urlpatterns = [
    path('chat', chat, name='chat'),
]
