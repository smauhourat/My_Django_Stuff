from django.conf.urls import url
from django.urls import path, re_path, include
from basic_app import views

# from django.conf import settings
# from django.conf.urls.static import static

app_name = 'basic_app'

urlpatterns = [
    re_path(r'^register/$', views.register, name='register'),
    re_path(r'^user_login/$', views.user_login, name='user_login'),
    # re_path(r'^other/$', views.other, name='other')
]
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
