from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Ambulance, Rating, Post

class UserRegistrationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['email', 'username', 'phone_number', 'is_driver', 'is_patient']

class AmbulanceForm(forms.ModelForm):
    class Meta:
        model = Ambulance
        fields = ['location', 'is_available', 'license_num']

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['ambulance', 'patient', 'rating', 'comment']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content']  
