from django.urls import path, re_path
from . import views as v

urlpatterns = [
    path('', v.HomePage.as_view(), name = 'url_home' ),
]