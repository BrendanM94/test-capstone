from django.urls import path
from . import views

urlpatterns = [
    path("", views.todo_list, name="todo_list"),
    path("complete/<int:pk>/", views.todo_complete, name="todo_complete"),
]