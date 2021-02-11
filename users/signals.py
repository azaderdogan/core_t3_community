from .models import *
from django.db.models.signals import post_save
from .api.serializers import ProfileSerializer
from django.dispatch import receiver

import random


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    print("creating", instance.id)

    city = City.objects.get(pk=int(random.random() * 50))
    school = School.objects.first()
    faculty = Faculty.objects.first()
    department = Department.objects.last()

    if created:
        Profile.objects.create(
            user=instance,
            biography="Milli Teknoloji Neferi",
            city=city,
            department=department,
            school=school,
            faculty=faculty,
            district=District.objects.first(),

        )


@receiver(post_save, sender=Profile)
def save_rosette(sender, instance, created, **kwargs):
    rosette = Rosette.objects.first()
    if rosette is None:
        rosette = Rosette.objects.create(rosette_name='Yeni Üye', rosette_number=1)

    instance.rosettes.add(rosette)
    print('roset atanıyor')
