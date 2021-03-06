# Generated by Django 2.1.7 on 2019-04-01 03:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('description', models.TextField(blank=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('due_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='TodoList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('completed', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='todoitem',
            name='list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todolist.TodoList'),
        ),
    ]
