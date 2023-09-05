from django.contrib import admin
from .models import CustomUser, Organization, Requisite, Adres


@admin.register(CustomUser)
class AdminCustomUser(admin.ModelAdmin):
    list_display = ('username',
                    'email',
                    'is_staff',
                    'organization'
    )


@admin.register(Organization)
class AdminOrganization(admin.ModelAdmin):
    list_display = (
        'name',
        'telephone',
        'requisite',
        'adres',
        'active',
        # 'get_adres_city',
    )

    # def get_adres_city(self, obj):
    #     if obj.requisite.adres is not None and obj.requisite.adres.city is not None:
    #         return obj.requisite.adres.city
    #     return 'Город не указан'
    
    # get_adres_city.short_description = 'Город'


@admin.register(Adres)
class AdminAdres(admin.ModelAdmin):
    list_display = (
        'city',
        'street',
        'house',
        'index',
    )


@admin.register(Requisite)
class AdminRequisite(admin.ModelAdmin):
    list_display = (
        'inn_nomber',
    )