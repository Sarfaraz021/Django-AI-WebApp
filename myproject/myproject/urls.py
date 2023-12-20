# myproject/urls.py
from django.contrib import admin
from django.urls import path, include
from myapp.views import chat, chat_view, chatAPI
from myapp import urls

app_name = 'myapp'

urlpatterns = [
    # path('chat/', chat, name='chat'),
    path("chat/", chat, name="chat"),
    path("admin/", admin.site.urls),
    path("chat/", include("myapp.urls")),
    path("chat_view/", chat_view, name="chat_view"),
    path("chatAPI/", chatAPI, name="chatAPI"),
]
