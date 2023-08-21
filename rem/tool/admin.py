from django.contrib import admin
from .models import (BaseMonitoringObject,
                     TypeMonitoringObject,
                     ViewMonitoringObject,
                     Production,
                     )

@admin.register(BaseMonitoringObject)
class BaseMonitoringObjectAdmin(admin.ModelAdmin):
    list_display = ('id_number',
                    'name',
                    'type',
                    'create_date',
                    
                    )
    search_fields = ('id_number',)
    list_filter = ('name', 'type',)


@admin.register(ViewMonitoringObject)
class ViewMonitoringAdmin(admin.ModelAdmin):
    list_display = ('view_name',)
    search_fields = ('view_name',)
    list_filter = ('view_name',)


@admin.register(TypeMonitoringObject)
class TypeMonitorinAdmin(admin.ModelAdmin):
    list_display = ('type_name',
                    'view')


@admin.register(Production)
class ProductionAdmin(admin.ModelAdmin):
    list_display = ('date_production', 'user', 'object')
