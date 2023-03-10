from django.shortcuts import render
from .models import DishCategory, Dish, About, Service,Gallery

# Create your views here.
def main_view(request):
    about = About.objects.get()
    services = Service.objects.filter(is_visible=True)
    galleries = Gallery.objects.all()
    return render(request, 'main_page.html', context={
        'about': about,
        'services': services,
        'galleries': galleries,
    })