from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import mixins
from users.models import Profile, Rosette, User
from users.api.serializers import ProfileSerializer, UserSerializer, RosetteSerializer, ProfilePhotoSerializer
from rest_framework import generics


# Create your views here.


