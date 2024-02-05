from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('key', include('appKey.urls')),
    path('summernote/', include('django_summernote.urls')),
    # static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)