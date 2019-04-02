from django.db import models
from datetime import datetime, timezone
from django.utils.timezone import localtime, now
import pytz

# Create your models here.


class TodoList(models.Model):
    title = models.CharField(max_length=120)
    completed = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    # def update_completed(self):
    #     '''returns number of completed items, total number of items'''
    #     items = TodoItem.objects.all()
    #     list=items.list(id=self.id)
    #     self.completed = 0
    #     counter = 0
    #     for i in items:
    #         counter += 1
    #         if i.done is True:
    #             self.completed += 1
    #     return self.completed/counter


class TodoItem(models.Model):
    list = models.ForeignKey(TodoList, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.name
        # if len(self.name) <= 10:
        #     return self.name
        # else:
        #     return f"{self.name[:10]}..."


    def days_left(self):
        '''Calculate how many days left before this item is due, or a warning string'''
        # now = datetime.now()
        # # dd/mm/YY H:M:S
        # dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        today = localtime(now())
        delta = (self.due_date - today)
        if delta.days > 0:
            return delta.days
        elif delta.days == 0:
            return f"Due today!"

        else:
            return "Overdue!!!"







