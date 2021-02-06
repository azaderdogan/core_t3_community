import os
import random

# pip install Faker & requests

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

import django

django.setup()

from users.api.serializers import UserSerializer

from faker import Faker
import requests


