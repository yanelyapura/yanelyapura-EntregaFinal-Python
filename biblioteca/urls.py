from django.contrib import admin
from django.urls import path, include
from libros.views import inicio

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='inicio'),  
    path('', include('libros.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
]
