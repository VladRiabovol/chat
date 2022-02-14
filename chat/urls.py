from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('chat/admin/', admin.site.urls),
    path('chat/', include('personal.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, documetnt_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, documetnt_root=settings.MEDIA_ROOT)