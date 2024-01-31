
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.mapa, name='mapa'),
path('', views.map_view, name='map_view'),
path('add_location/', views.add_location, name='add_location'),
path('get_locations/', views.get_locations, name='get_locations'),



]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)