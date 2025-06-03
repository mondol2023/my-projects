from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        if not username:
            raise ValueError("The Username field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, username, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    is_driver = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)

    # Required flags for using Django's admin and permissions system
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    # Use email as the unique identifier for authentication
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

# Your other models (Ambulance, Rating, Post) can remain similar, but make sure they reference the updated User model.

class Ambulance(models.Model):
    # The driver should be a user flagged as a driver
    driver = models.OneToOneField(User, on_delete=models.CASCADE, related_name='ambulance')
    location = models.CharField(max_length=255, blank=True, null=True)
    is_available = models.BooleanField(default=True)
    license_num = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"Ambulance driven by {self.driver.phone_number} - {'Available' if self.is_available else 'Not Available'}"

class Rating(models.Model):
    ambulance = models.ForeignKey(Ambulance, on_delete=models.CASCADE, related_name='ratings')
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')
    rating = models.PositiveIntegerField()
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
