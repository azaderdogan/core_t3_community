from django.contrib.auth.models import AbstractBaseUser
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin)

from django.db import models

from PIL import Image
from utils.models import *

class UserManager(BaseUserManager):

    def create_user(self, username, email, password=None):
        if username is None:
            raise TypeError('Users should have a username')
        if email is None:
            raise TypeError('Users should have a Email')
        if password is None:
            raise TypeError('Users should have a Password')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password=None):
        if password is None:
            raise TypeError('Password should not be none')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True, db_index=True)
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    first_name = models.CharField(max_length=200, null=False)
    last_name = models.CharField(max_length=200, null=False)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', ]

    objects = UserManager()

    def __str__(self):
        return self.username


class Rosette(models.Model):
    rosette_name = models.CharField(max_length=300, blank=False, null=False)
    create_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    rosette_number = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    def __str__(self):
        return self.rosette_name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    biography = models.TextField(blank=True, null=True)
    profile_photo = models.ImageField(null=True, blank=True, upload_to='profile_photos/%Y/%m/')
    birth_of_date = models.DateField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    tc_number = models.CharField(max_length=30, blank=True, null=True)  # unique=True
    create_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)

    school = models.ForeignKey(School, on_delete=models.DO_NOTHING)
    faculty = models.ForeignKey(Faculty, on_delete=models.DO_NOTHING)
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING, null=True)

    city = models.ForeignKey(City, on_delete=models.DO_NOTHING, null=True)
    district = models.ForeignKey(District, on_delete=models.DO_NOTHING)

    rosettes = models.ManyToManyField(Rosette, related_name='rosettes', blank=True)

    class Meta:
        verbose_name_plural = 'kullanıcı_profilleri'

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        self.id = self.user.id
        # ımage resize
        super().save(*args, **kwargs)

        if self.profile_photo:  # eğer foto varsa
            img = Image.open(self.profile_photo.path)
            if img.height > 600 or img.width > 600:
                output_size = (600, 600)
                img.thumbnail(output_size)
                img.save(self.profile_photo.path)
