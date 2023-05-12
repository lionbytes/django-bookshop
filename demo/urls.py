from django.urls import path
from . import views

urlpatterns = [
    path('first', views.first),
    path('second', views.Second.as_view()),
    path('third', views.third),
]