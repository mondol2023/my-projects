from django.db import models


class VehicleRegistration(models.Model):
    CAR = "car"
    BUS = "bus"
    MINI_BUS = "mini_bus"
    BIKE = "bike"
    MICRO = "micro"
    TRUCK = "truck"
    VEHICLE_TYPE_CHOICES = {
        CAR: "Car",
        BUS: "Bus",
        MINI_BUS: "Mini Bus",
        BIKE: "Bike",
        MICRO: "Micro",
        TRUCK: "Truck",
    }
    
    vehicle_name = models.CharField(max_length=50, blank=True, null=True)
    vehicle_model = models.CharField(max_length=50)
    vehicle_license = models.CharField(max_length=100)
    vehicle_type = models.CharField(
        max_length=30,
        choices=VEHICLE_TYPE_CHOICES,
        default=CAR,
    )
    vehicle_image = models.FileField(upload_to="media/images/", blank=True, null=True)
    vehicle_length = models.FloatField()

    vehicle_width = models.FloatField()
    vehicle_height = models.FloatField()
    driver_name = models.CharField(max_length=100)
    driver_phone = models.CharField(max_length=14)
    driver_license = models.CharField(max_length=100)
    owner_name = models.CharField(max_length=100, blank=True, null=True)
    owner_phone = models.CharField(max_length=14, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "vehicle_registration"
        verbose_name = "Vehicle Registration"
        verbose_name_plural = "Vehicle Registrations"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.vehicle_model } - {self.vehicle_license}"
    