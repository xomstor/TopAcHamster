from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name="url-home"),
]