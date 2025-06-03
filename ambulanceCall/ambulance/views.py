from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView, FormView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from .models import Ambulance, User, Rating, Post
from .forms import UserRegistrationForm, AmbulanceForm, RatingForm, PostForm
from django.contrib.auth.forms import AuthenticationForm

class RegisterView(FormView):
    template_name = 'templates/register.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class CustomLoginView(LoginView):
    template_name = 'templates/login.html'
    success_url = reverse_lazy('home')
    form_class = AuthenticationForm

class CustomLogoutView(LogoutView):
    template_name = 'templates/logout.html'
    next_page = reverse_lazy('login')

class HomeView(TemplateView):
    template_name = 'templates/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ambulances'] = Ambulance.objects.all()
        return context

class AmbulanceListView(ListView):
    model = Ambulance
    template_name = 'templates/ambulance_list.html'
    context_object_name = 'ambulances'

    def get_queryset(self):
        location = self.request.GET.get('location')
        if location:
            return Ambulance.objects.filter(location__icontains=location, is_available=True)
        return Ambulance.objects.all()

class AmbulanceCreateView(CreateView):
    model = Ambulance
    form_class = AmbulanceForm
    template_name = 'templates/ambulance_form.html'
    success_url = reverse_lazy('ambulance_list')
     
    def form_valid(self, form):
        form.instance.driver = self.request.user
        return super().form_valid(form)

class RatingCreateView(CreateView):
    model = Rating
    form_class = RatingForm
    template_name = 'templates/rating_form.html'
    success_url = reverse_lazy('ambulance_list')

    def form_valid(self, form):
        
        form.instance.patient = self.request.user
        return super().form_valid(form)

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'templates/post_form.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class UserProfileView(TemplateView):
    template_name = 'templates/user_profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context

class PostListView(ListView):
    model = Post
    template_name = 'templates/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user).order_by('-created_at')
