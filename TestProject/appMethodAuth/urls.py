from django.urls import path
from . import views

urlpatterns = [
    path('auth', views.AuthPage.as_view(), name = 'url-methodauth'),
    path('', views.AccountPage.as_view(), name = 'url-account'),
    path('logout', views.LogoutPage.as_view(), name = 'url-logout'),
    path('reg', views.RegPage.as_view(), name = 'url-reg'),
]