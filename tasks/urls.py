from django.urls import path
from . import views

urlpatterns = [
    path('tasks/create/', views.create, name="create")
]
