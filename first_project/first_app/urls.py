from django.conf.urls import url
from django.urls import re_path
from first_app import views

urlpatterns = [
    re_path(r'^$', views.index)
]