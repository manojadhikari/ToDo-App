from django.views import generic
from .models import Task

class IndexView(generic.ListView):
    template_name = 'todoapp/index.html'

    def get_queryset(self):
        return Task.objects.all()

class DetailView(generic.DetailView):
    model = Task
    template_name = 'todoapp/detail.html'
