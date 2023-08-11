from django.contrib import admin
from .models import ViewEquipment, TypeEquipment, BaseMonitoringObject, UniqueIdentificator
from django.db import models


@admin.register(UniqueIdentificator)
class UniqueIdentificatorAdmin(admin.ModelAdmin):
    pass

@admin.register(ViewEquipment)
class ViewEquipmentAdmin(admin.ModelAdmin):
    pass


@admin.register(TypeEquipment)
class TypeEquipmentAdmin(admin.ModelAdmin):
    pass


@admin.register(BaseMonitoringObject)
class BaseMonitoringObjectAdmin(admin.ModelAdmin):
    list_filter = ('name', 'type',)
    list_display = ('name', 'type', 'type_name')

    def type_name(self, obj):
        return obj.type.view.name
