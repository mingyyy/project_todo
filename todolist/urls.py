from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "todolist"

urlpatterns = [
    path('', views.home, name="home_page"),
    path('todo/', views.index, name="index_page"),
    path('todo/<int:list_id>',views.list, name="list_page"),
    path('update/<int:list_id>',views.update_item, name="update_item_page"),
    path('test/<int:list_id>',views.test_item, name="test_page"),
]