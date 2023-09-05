from django.contrib import admin
from .models import (BaseMonitoringObject,
                     TypeMonitoringObject,
                     ViewMonitoringObject,
                     Production,
                     QRCode,
                     )

@admin.register(BaseMonitoringObject)
class BaseMonitoringObjectAdmin(admin.ModelAdmin):
    list_display = ('qrcode',
                    'name',
                    'type',
                    'get_type_view',
                    'production',
                    'active'
                    )
    search_fields = ('qrcode__unique_number',)
    list_filter = ('name',
                   'type',
                   'type__view',)

    def get_type_view(self, obj):
        return obj.type.view
    
    get_type_view.short_description = 'View'


@admin.register(ViewMonitoringObject)
class ViewMonitoringAdmin(admin.ModelAdmin):
    list_display = ('view_name',)
    search_fields = ('view_name',)
    list_filter = ('view_name',)


@admin.register(TypeMonitoringObject)
class TypeMonitorinAdmin(admin.ModelAdmin):
    list_display = ('type_name',
                    'view',
                    )


@admin.register(Production)
class ProductionAdmin(admin.ModelAdmin):
    list_display = ('create_date',
                    'related_base_monitoring_object',
                    'organization',
                    'collector',
                    )

    def related_base_monitoring_object(self, obj):
        if obj.basemonitoringobject_set.exists():
            base_monitoring_object = obj.basemonitoringobject_set.first()
            return f"{base_monitoring_object.name} (ID: {base_monitoring_object.id})"
        return "Нет связанных объектов"
    related_base_monitoring_object.short_description = "Связанный объект BaseMonitoringObject"


@admin.register(QRCode)
class QRCodeAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'unique_number',
                    'related_base_monitoring_object',
                    )

    def related_base_monitoring_object(self, obj):
        if obj.basemonitoringobject_set.exists():
            base_monitoring_object = obj.basemonitoringobject_set.first()
            return f"{base_monitoring_object.name} (ID: {base_monitoring_object.id})"
        return "Нет связанных объектов"
    related_base_monitoring_object.short_description = "Связанный объект BaseMonitoringObject"
