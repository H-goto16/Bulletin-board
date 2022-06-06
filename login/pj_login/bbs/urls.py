from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, re_path
from django.conf import settings
from django.views.static import serve 


app_name    = "bbs"
urlpatterns = [
    path('', views.index, name="index"),
        re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]