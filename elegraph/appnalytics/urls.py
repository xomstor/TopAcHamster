from django.urls import path
from . import views

urlpatterns = [
    path('<slug:name_link>', views.UALinkPage.as_view(), name='url-staticlinkpage'),
]