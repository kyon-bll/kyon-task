from django.conf.urls import include, url
from . import views

name_app='task'
urlpatterns = [
    url(r'^$', views.task_list, name='index'),
]
