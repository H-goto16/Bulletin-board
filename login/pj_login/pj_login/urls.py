from django.contrib import admin
from django.urls import path, include
from django.urls import path, include, re_path
from django.contrib.auth.decorators import login_required
from registration import views
from django.views.static import serve 
from django.conf import settings
from django.views.generic import TemplateView

index_view = TemplateView.as_view(template_name="registration/index.html")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("bbs.urls")),
    path("", login_required(index_view), name="index"),
    path('', include("django.contrib.auth.urls")),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path('activate/<uidb64>/<token>/', views.ActivateView.as_view(), name='activate'),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]