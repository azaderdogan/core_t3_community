from .models import *
from django.db.models.signals import post_save
from .api.serializers import ProfileSerializer
from django.dispatch import receiver


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    print("creating",instance.id)

    city = City.objects.get(pk=instance.id)
    school = School.objects.get(pk=instance.id)
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
