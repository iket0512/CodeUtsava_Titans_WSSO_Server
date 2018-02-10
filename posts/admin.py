# Register your models here.
from django.contrib import admin

# Register your models here.
from django.apps import apps


myapp = apps.get_app_config('posts')
for model in myapp.get_models():
	admin.site.register(model)