from django import forms
from .models import TodoItem,TodoList


class UpdateItems(forms.ModelForm):
    class Meta:
        model = TodoItem
        fields = ["done"]

class UpdateList(forms.ModelForm):
    class Meta:
        model=TodoList
        fields=["completed"]

