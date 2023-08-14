from django.contrib import admin
from .models import BaseMonitoringObject

@admin.register(BaseMonitoringObject)
class BaseMonitoringObjectAdmin(admin.ModelAdmin):
    list_display = ('id_number', 'name', 'id')
