from django.urls import path
from . import views


urlpatterns = [
    path("addTask/", views.addTask, name="addTask"),
    path("mark-as-done/<int:id>/", views.mark_as_done, name="mark_as_done"),
    path("mark-as-undone/<int:id>/", views.mark_as_undone, name="mark_as_undone"),
    path("edit-task/<int:id>", views.edit_task, name="edit_task"),
    path("delete-task/<int:id>", views.delete_task, name="delete_task")
]