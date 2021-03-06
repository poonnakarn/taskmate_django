from django.shortcuts import render, redirect
from django.http import HttpResponse
from todolist_app.models import TaskList
from todolist_app.forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.
def todolist(request):
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.save()
        messages.success(request, ("New Task Added!"))
        return redirect("todolist")
    else:
        # GET request
        all_tasks = TaskList.objects.all()
        paginator = Paginator(all_tasks, 5)  # using page of 5
        page = request.GET.get("page")
        all_tasks = paginator.get_page(page)

        return render(request, "todolist.html", {"all_tasks": all_tasks})


def delete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    task.delete()
    return redirect("todolist")


def edit_task(request, task_id):
    if request.method == "POST":
        # POST request
        task = TaskList.objects.get(pk=task_id)
        form = TaskForm(request.POST or None, instance=task)
        if form.is_valid():
            form.save()

        messages.success(request, ("Task Edited!"))
        return redirect("todolist")
    else:
        # GET request
        task_obj = TaskList.objects.get(pk=task_id)
        return render(request, "edit.html", {"task_obj": task_obj})


def complete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    task.done = True
    task.save()
    return redirect("todolist")


def pending_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    task.done = False
    task.save()
    return redirect("todolist")


def contact(request):
    context = {
        "welcome_text": "Welcome to Contact Page.",
    }
    return render(request, "contact.html", context)


def about(request):
    context = {
        "welcome_text": "Welcome to About Page.",
    }
    return render(request, "about.html", context)


def index(request):
    context = {
        "index_text": "Welcome to Index Page.",
    }
    return render(request, "index.html", context)
