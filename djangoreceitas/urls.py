from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

print(include('apps.recetas.urls'))

urlpatterns = [
    path('', include('apps.home.urls')),
    path('recetas/', include('apps.recetas.urls')),
    path('usuarios/', include('apps.usuarios.urls')),
    path('admin/', admin.site.urls),
    path('custom-url/', include('drf_expiring_token.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
