from django.urls import path
from .views import VehicleRegistrationAPIView

urlpatterns = [
    # path('/admin/', views.vehicle_registration, name='vehicle_registration'),
    path('/admin/', VehicleRegistrationAPIView.as_view(), name='car-list-create'),         # GET (list), POST (create)
    path('/admin/<int:pk>/', VehicleRegistrationAPIView.as_view(), name='car-detail-update-delete'),  # GET (retrieve), PUT (update), DELETE (delete)
]
