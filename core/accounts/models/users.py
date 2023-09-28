from django.db import models
from django.contrib.auth.models import (
    User,
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db.models.signals import post_save


class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(" the email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_verified", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("superuser must be is_staff=true")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("superuser must be is_superuser=true")
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    # custom user model
    # def create_user(self, email, password):
    #     self.email = email
    #     self.password = password

    email = models.EmailField(max_length=255, unique=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELD = []

    created_Date = models.DateField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    object = UserManager()

    def __str__(self):
        return self.email
