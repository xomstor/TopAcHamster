
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('analytics/', include('appnalytics.urls')),
    path('', include('appPublication.urls')),
]
