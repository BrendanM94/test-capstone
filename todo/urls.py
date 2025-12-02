from django.urls import path
from . import views

urlpatterns = [
    path("", views.todo_list, name="todo_list"),
    path("complete/<int:pk>/", views.todo_complete, name="todo_complete"),
    path("delete/<int:pk>/", views.todo_delete, name="todo_delete"),
    path("edit/<int:pk>/", views.todo_edit, name="todo_edit"),
]