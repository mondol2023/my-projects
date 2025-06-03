from django.urls import path
from .views import AmbulanceView, AmbulanceCreateView, register_view, LoginView, LogoutView, HomeView

urlpatterns = [
    path('', AmbulanceView.as_view(), name='ambulance_list'),
    path('ambulance/create/', AmbulanceCreateView.as_view(), name='ambulance_create'),
    path('register/', register_view.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('home/', HomeView.as_view(), name='home'),
]