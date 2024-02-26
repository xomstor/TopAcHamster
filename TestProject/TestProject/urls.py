from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('grappelli/', include('grappelli.urls')),
    path('', include('appKey.urls')),
    path('api/', include('appApi.urls')),
    path('auth/', include('appAuth.urls')),
    path('summernote/', include('django_summernote.urls')),
    # static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)