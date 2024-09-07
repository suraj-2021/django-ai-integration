from django.urls import path
from . import views

app_name = "aiapp"

urlpatterns = [
     path("chat/",views.chat,name='chat'),
]