from django.conf.urls import url
from django.urls import path, re_path, include
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    # re_path(r'^$', views.index)
    re_path(r'^relative/$', views.relative),
    re_path(r'^other/$', views.other, name='other')
]
