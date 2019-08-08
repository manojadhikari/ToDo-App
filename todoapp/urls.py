from django.conf.urls import url
from django.contrib import admin
from todoapp import views

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),#index is the function name in the views.py file
    url(r'^(?P<task_id>[0-9]+)/$', views.detail, name='detail'),
]