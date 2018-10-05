from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="schedule-home"),
    path('schedule/', views.schedule, name="schedule-schedule"),
]
