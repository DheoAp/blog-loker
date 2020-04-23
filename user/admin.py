from django.contrib import admin

# Register your models here.
from .models import ModelData,InfoModel

class AdminLoker(admin.ModelAdmin):
    readonly_field = ['slug','publish']

admin.site.register(ModelData,AdminLoker)
admin.site.register(InfoModel,AdminLoker)