from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Todo


@login_required
def todo_list(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description", "")

        # super simple validation: only create if there's a title
        if title:
            Todo.objects.create(
    user=request.user,
    title=title,
    description=description
)


        # redirect so refresh doesn't re-submit the form
        return redirect("todo_list")

    # GET request: just show the list
    todos = Todo.objects.filter(user=request.user).order_by("-created_at")
    return render(request, "todo/todo_list.html", {"todos": todos})

@login_required
def todo_complete(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.completed = True
    todo.save()
    return redirect("todo_list")

@login_required
def todo_delete(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()
    return redirect("todo_list")

@login_required
def todo_edit(request, pk):
    todo = Todo.objects.get(pk=pk, user=request.user)

    if request.method == "POST":
        todo.title = request.POST.get("title")
        todo.description = request.POST.get("description", "")
        todo.save()
        return redirect("todo_list")

    return render(request, "todo/todo_edit.html", {"todo": todo})
