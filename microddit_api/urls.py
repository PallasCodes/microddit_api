from django.contrib import admin
from django.urls import path, include
from django.config import settings
from django.config.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')),
    path('api/v1/', include('post.urls')),
    path('api/v1/communities/', include('communitie.urls')),
    path('api/v1/', include('myuser.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
