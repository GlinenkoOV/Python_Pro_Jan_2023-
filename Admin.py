from django.contrib import admin
from .models import DishCategory, Dish, About, Service,Gallery

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display =['heading', 'desc_history']

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display =['title', 'position', 'desc', 'is_visible']

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['title', 'image']