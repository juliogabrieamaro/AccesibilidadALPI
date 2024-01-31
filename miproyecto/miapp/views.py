from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from .forms import LocationForm
from django.http import JsonResponse
from django.core.serializers import serialize
from .models import Location, Category

def mapa(request):
    return render(request, 'miapp/mapa.html')

# views.py
def map_view(request):
    category_filter = request.GET.get('category', '')
    locations = Location.objects.all()

    if category_filter:
        locations = locations.filter(category__name=category_filter)

    categories = Category.objects.all()

    return render(request, 'miapp/mapa.html', {'locations': locations, 'category_filter': category_filter, 'categories': categories })



def get_locations(request):
    locations = Location.objects.all()

    locations_data = [
        {
            'latitude': location.latitude,
            'longitude': location.longitude,
            'name': location.name,
            'description': location.description,
            'category': location.category.name if location.category else None,
            'image_url': location.image.url if location.image else None,
        }
        for location in locations
    ]

    categories_data = serialize('json', Category.objects.all())  # Serialize categories to JSON

    return JsonResponse({'locations': locations_data, 'categories': categories_data})


@csrf_protect
def add_location(request):
    if request.method == 'POST':
        form = LocationForm(request.POST, request.FILES)
        if form.is_valid():
            new_location = form.save()
            messages.success(request, 'Ubicación agregada exitosamente.')
            print(f'Ubicación guardada: {new_location}')  # Verifica en la consola
            return redirect('map_view')
        else:
            messages.error(request, 'Error al agregar la ubicación. Verifica los campos.')
            print(form.errors)  # Imprime errores en la consola
    else:
        form = LocationForm()

    return render(request, 'miapp/mapa.html', {'form': form})
