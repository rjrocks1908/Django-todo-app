from django.shortcuts import redirect, get_object_or_404, render
from todo.models import Task


def addTask(request):
    task = request.POST["task"]
    Task.objects.create(task=task)
    return redirect("home")


def mark_as_done(request, id):
    task = get_object_or_404(Task, id=id)
    task.is_completed = True
    task.save()
    return redirect("home")


def mark_as_undone(request, id):
    task = get_object_or_404(Task, id=id)
    task.is_completed = False
    task.save()
    return redirect("home")


def edit_task(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == "POST":
        task.task = request.POST["task"]
        task.save()
        return redirect("home")
    else:
        context = {"task": task}
        return render(request, "edit_task.html", context)
