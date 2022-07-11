from django.shortcuts import render
from django.http import HttpResponse
from .models import Todo
import time
from plyer import notification
from threading import *

def mythread():
    while True:
        notification.notify(
            title = "**Please Check Your ToDo list!!!",
            message = "May be there is some important work you have added in your ToDo.",
            timeout =10
            )
        time.sleep(60)

t=Thread(target=mythread)
t.start()

def index(request):
    list_todo = Todo.objects.filter(status=False)
    return render(request, 'base.html', {'list_todo': list_todo})


def mark_as_done(request, id):
    obj = Todo.objects.get(pk=id)
    obj.status = True
    obj.save()
    list_todo = Todo.objects.filter(status=False)
    return render(request, 'base.html', {'list_todo': list_todo})


def new_todo(request):
    if request.method == "POST":
        Todo.objects.create(name=request.POST.get('todo-name'))
        list_todo = Todo.objects.filter(status=False)
        return render(request, 'base.html', {'list_todo': list_todo})
