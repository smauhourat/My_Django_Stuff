from django.conf.urls import url
from django.urls import path, re_path, include
from second_app import views

urlpatterns = [
    # re_path(r'^$', views.index)
    re_path(r'^$', views.users)
]