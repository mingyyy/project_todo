from django.shortcuts import render, redirect, get_object_or_404
from .models import TodoList,TodoItem
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import UpdateItems, UpdateList
from django.contrib import messages

# Create your views here.


def home(request):
    # context={"dummy": [{"list": 'dfads'}]}
    return render(request, "todolist/home.html")


def index(request):
    todo=TodoList.objects.order_by("title")
    lists={}
    for l in todo:
        items = l.todoitem_set.all()
        n = 0
        total =0
        for item in items:
            total += 1
            if item.done is True:
                n += 1
        lists[l] = n/total
    context = {"lists": lists}
    return render(request, "todolist/index.html", context)


def list(request, list_id):
    todo = TodoList.objects.get(id=list_id)
    num_completed = todo.completed
    print(num_completed)
    print(request.POST.getlist("done"))
    for i in request.POST.getlist("done"):
        todoitem=todo.todoitem_set.get(id=i)
        todoitem.done=True
        todoitem.save()
        num_completed += 1
    todo.completed = num_completed
    todo.save()

    context = {"list":todo}
    return render(request, 'todolist/todo.html', context)


def update_item(request, list_id):
    list_content = TodoList.objects.get(id=list_id)
    items=TodoItem.objects.filter(list=list_id)
    # print(request.POST)
    context = {"list": list_content, "items":items, "listid":list_id}
    return render(request, 'todolist/update_item.html', context)


def test_item(request, list_id):
    todo = TodoList.objects.get(id=list_id)
    num_completed = todo.completed
    print(num_completed)
    print(request.POST.getlist("done"))
    for i in request.POST.getlist("done"):
        todoitem=todo.todoitem_set.get(id=i)
        todoitem.done=True
        todoitem.save()
        num_completed += 1
    todo.completed = num_completed
    todo.save()

    context = {"list":todo}
    return render(request, 'todolist/test.html', context)
