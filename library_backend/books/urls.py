from django.urls import path
from .views import booksListView

urlpatterns = [
    path('', booksListView.as_view(), name='home'),  
]