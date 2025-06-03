from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Ambulance, Rating, Post
from django.utils.translation import gettext_lazy as _
from django import forms

# Optional: Custom form to control what fields show in admin
class UserAdminForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

# Custom admin for User model
class UserAdmin(BaseUserAdmin):
    form = UserAdminForm
    model = User
    list_display = ('email', 'username', 'phone_number', 'is_driver', 'is_patient', 'is_staff', 'is_superuser')
    list_filter = ('is_driver', 'is_patient', 'is_staff', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        (_('Personal info'), {'fields': ('phone_number', 'location')}),
        (_('Roles'), {'fields': ('is_driver', 'is_patient')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'phone_number', 'password1', 'password2', 'is_driver', 'is_patient')}
        ),
    )
    search_fields = ('email', 'username', 'phone_number')
    ordering = ('email',)

# Register custom User model
admin.site.register(User, UserAdmin)

# Register other models
@admin.register(Ambulance)
class AmbulanceAdmin(admin.ModelAdmin):
    list_display = ('driver', 'location', 'is_available', 'license_num')
    list_filter = ('is_available',)

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('ambulance', 'patient', 'rating', 'created_at')
    list_filter = ('rating',)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'created_at')
    search_fields = ('author__email', 'content')

