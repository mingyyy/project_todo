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
    todoitems = todo.todoitem_set.all()
    getitems = get_object_or_404(TodoList, id=list_id)
    try:
        selected_item=getitems.todoitem_set.get(id=request.POST['item.id'])
    except(KeyError, TodoItem.DoesNotExist):
        pass
    else:
        selected_item.done = True
        selected_item.save()

    getitems.completed.save()

    if request.method == 'POST':
        form = request.POST()
        if form.is_valid():
            form.save()
            todoitems = todo.todoitem_set.all()

    context = {"list":todo,"items": todoitems}
    return HttpResponseRedirect(reverse('todolist:test_page', args=(list.id,)))

def finish(request, item_id):
    item = TodoItem.objects.get(id=item_id)
    item.done = True
    item.save()
    return redirect("todolist/todo.html")


def update_item(request, list_id):

    list_content = TodoList.objects.get(id=list_id)
    items=TodoItem.objects.filter(list=list_id)
    # print(request.POST)
    context = { "list": list_content, "items":items, "listid":list_id}
    return render(request, 'todolist/update_item.html', context)


def test_item(request, list_id):
    todo = TodoList.objects.get(id=list_id)
    context = {"list":todo}
    print(request.POST)
    return render(request, 'todolist/test.html', context)
