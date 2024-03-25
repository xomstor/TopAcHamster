from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name = 'url-homepage'),
    path('method-django-post/', views.MethodDjangoPost.as_view(), name = 'url-method-django-post'),
    path('method-ajax-post/', views.MethodAjaxPost.as_view(), name = 'urlMethodAjaxPost'),

]