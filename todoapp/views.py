# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse, Http404
from django.template import loader

from .models import Task
# Create your views here.
def index(request):
    task_list = Task.objects.all()
    context = {
        'task_list': task_list
    }
    return render(request, 'todoapp/index.html', context)

def detail(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)
    except Task.DoesNotExist:
        raise Http404 ('This task does not exist')

    context = {
        'task': task
    }
    return render(request, 'todoapp/detail.html', context)