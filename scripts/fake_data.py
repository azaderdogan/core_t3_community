import os
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core_t3.settings')

import django

django.setup()

from users.models import *
from utils.models import *

from faker import Faker


fake = Faker(['tr_TR'])


def set_user():
    f_name = fake.first_name()
    l_name = fake.last_name()
    u_name = f'{f_name.lower()}_{l_name.lower()}'
    user_check = User.objects.filter(username=u_name)
    email = f'{u_name}@{fake.domain_name()}'
    while user_check.exists():
        u_name = f'{f_name.lower()}_{l_name.lower()}'
        user_check = User.objects.filter(username=u_name)
        email = f'{u_name}@{fake.domain_name()}'
    pswd = fake.msisdn()

    user = User(
        username=u_name,
        last_name=l_name,
        first_name=f_name,
        email=email,
        is_staff=fake.boolean(chance_of_getting_true=50),
    )
    user.set_password(pswd)
    user.save()
    print(f"{u_name} kullanıcısı kaydedildi.")


import json

from pprint import pprint


def init_cities():
    country = Country(
        country_code=90,
        country_name='Türkiye'
    )
    country.save()

    file = open('scripts/il-ilce.json')
    data = json.load(file)

    for city in data['data']:
        il_adi = city['il_adi']
        plaka_kodu = city['plaka_kodu']

        city_instance = City(
            country=country,
            city_name=il_adi,
            plate_code=plaka_kodu
        )
        city_instance.save()

        for district in city['ilceler']:
            ilce_adi = district['ilce_adi']
            district_instance = District(
                district_name=ilce_adi,
                city=city_instance
            )
            district_instance.save()


def init_schools():
    pass
