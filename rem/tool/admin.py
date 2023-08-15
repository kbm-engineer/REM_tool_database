from django.contrib import admin
from .models import BaseMonitoringObject

@admin.register(BaseMonitoringObject)
class BaseMonitoringObjectAdmin(admin.ModelAdmin):
    list_display = ('id_number',
                    'name',
                    'create_date',
                    'update_date',
                    'start_date_use',
                    'days_warranty',)
