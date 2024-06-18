from django.urls import path
from .import views

# URL_config
urlpatterns = [
    path('hello/', views.say_hello)
]