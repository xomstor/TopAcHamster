from django.urls import path
from . import views

urlpatterns = [
    path('', views.PublicationPage.as_view(), name='url-publication'),
    path('<slug:url_name_pub>', views.OpenPublicPage.as_view(), name='url-open-publication'),
]