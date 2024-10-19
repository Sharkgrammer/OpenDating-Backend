from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)

# System Models
from core.functions.gen_functions import get_today, generate_random_string


class SystemUserManager(BaseUserManager):
    def create_user(self, email, full_name, display_name, password=None, commit=True):

        if not email:
            raise ValueError('Users must have an email address')
        if not full_name:
            raise ValueError('Users must have a full name')
        if not display_name:
            raise ValueError('Users must have a display name')

        user = self.model(
            email=self.normalize_email(email),
            full_name=full_name,
            display_name=display_name,
        )

        user.set_password(password)
        if commit:
            user.save(using=self._db)

        return user

    def create_superuser(self, email, full_name, display_name, password):

        user = self.create_user(
            email,
            password=password,
            full_name=full_name,
            display_name=display_name,
            commit=False,
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    id = models.BigAutoField(primary_key=True)
    uid = models.CharField(max_length=10, unique=True, default=generate_random_string)

    email = models.EmailField('Email', max_length=255, unique=True)

    # Personal data
    full_name = models.CharField('Full Name', max_length=255, blank=True)
    display_name = models.CharField('Display Name', max_length=30, blank=True)
    description = models.TextField(verbose_name='Description', blank=True)

    # TODO deal with interest data

    # Admin data
    is_active = models.BooleanField('Active', default=True)
    is_admin = models.BooleanField('Admin Status', default=False)
    is_staff = models.BooleanField('Staff Status', default=False)

    date_joined = models.DateTimeField(verbose_name='Date Joined', default=get_today)
    last_login = models.DateTimeField(verbose_name='Last Login', default=get_today)
    deleted = models.BooleanField(default=False)

    objects = SystemUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name', 'display_name']

    def __str__(self):
        return f"{self.full_name} ({self.uid})"
