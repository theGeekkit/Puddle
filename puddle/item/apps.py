from django.apps import AppConfig


class ItemConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'item'
    
    def ready(self):
        from .models import Category
        
        from django.contrib import admin
        admin.site.register(Category)
