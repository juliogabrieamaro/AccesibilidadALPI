

# miproyecto/urls.py
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('miapp.urls')),  # Asegúrate de que 'miapp' sea el nombre correcto de tu aplicación
]
