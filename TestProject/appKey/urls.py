from django.urls import path
from . import views
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

urlpatterns = [
    # path('', views.HomeKey.as_view(), name='url-home'),
    path('', views.CategoriesPage.as_view(), name='url-categories'),
    path('category/<int:id>', views.ProductPage.as_view(), name='url-product'),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('images/favicon.ico'))),
    path('search', views.Search.as_view(), name='url-search'),
]