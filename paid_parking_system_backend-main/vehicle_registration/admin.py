from django.contrib import admin
from .models import VehicleRegistration

@admin.register(VehicleRegistration)
class VehicleRegistrationAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'vehicle_name',
        'vehicle_model',
        'vehicle_license',
        'vehicle_type',
        'vehicle_image',
        'vehicle_length',   
        'vehicle_width',
        'vehicle_height',
        'driver_name',
        'driver_phone',
        'driver_license',
        'owner_name',
        'owner_phone',
    ]
