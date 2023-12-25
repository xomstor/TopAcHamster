from django.urls import path
from . import views

urlpatterns = [
    path('', views.Hamsterhome.as_view(), name='index'),
]