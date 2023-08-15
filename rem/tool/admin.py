from django.contrib import admin
from .models import (BaseMonitoringObject, Guarantee)

@admin.register(BaseMonitoringObject)
class BaseMonitoringObjectAdmin(admin.ModelAdmin):
    list_display = ('id_number',
                    'name',
                    'create_date',
                    'update_date',
                    'start_date_use',
                    'end_warranty',
                    'days_warranty',
                    )


@admin.register(Guarantee)
class AdminGuarantee(admin.ModelAdmin):
    list_display = ('object',)