from django.urls import path, re_path
from . import views as v

urlpatterns = [
    path('', v.HomePage.as_view(), name = 'url_home' ),
    re_path(r'news/?$', v.NewsPage.as_view(), name = 'url_news' ),
    re_path(r'offer/?$', v.OfferPage.as_view(), name = 'url_offer' ),
]