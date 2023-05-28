from django.contrib import admin
from django.apps import apps
from django.contrib.admin.sites import AlreadyRegistered

# Register your models here.

models = apps.get_app_config('controlmarcaciones').get_models()
for model in models:
    try:
        admin.site.register(model)
    except AlreadyRegistered:
        pass