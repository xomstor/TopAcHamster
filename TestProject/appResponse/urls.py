from django.urls import path, re_path
from . import views


urlpatterns = [
    re_path(r'', views.ResponsePage.as_view(), name='url-response'),
    ]
