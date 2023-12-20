# myapp/urls.py
from django.urls import path
from .views import chat, chat_view, chatAPI

app_name = 'myapp'

urlpatterns = [
    path('chat/', chat, name='chat'),
    path('chat_view/', chat_view, name='chat_view'),
    path('chatAPI/', chatAPI, name='chatAPI'),
    # Add other URL patterns as needed
]
