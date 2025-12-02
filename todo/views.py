from django.shortcuts import render, redirect
from .models import Todo


def todo_list(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description", "")

        # super simple validation: only create if there's a title
        if title:
            Todo.objects.create(title=title, description=description)

        # redirect so refresh doesn't re-submit the form
        return redirect("todo_list")

    # GET request: just show the list
    todos = Todo.objects.all().order_by("-created_at")
    return render(request, "todo/todo_list.html", {"todos": todos})

def todo_complete(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.completed = True
    todo.save()
    return redirect("todo_list")

def todo_delete(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()
    return redirect("todo_list")
