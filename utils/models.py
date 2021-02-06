from django.db import models


# Create your models here.

class Country(models.Model):
    country_code = models.IntegerField()
    country_name = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.country_name


class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    city_name = models.CharField(max_length=200)
    plate_code = models.IntegerField(unique=True, null=False, blank=False)

    def __str__(self):
        return self.city_name


class District(models.Model):
    district_name = models.CharField(max_length=200, null=False, blank=False)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return self.district_name


class School(models.Model):
    school_name = models.CharField(max_length=300, null=False, blank=False)

    def __str__(self):
        return self.school_name


class Faculty(models.Model):
    faculty_name = models.CharField(max_length=300, null=False, blank=False)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return self.faculty_name


class Department(models.Model):
    department_name = models.CharField(max_length=200)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)

    def __str__(self):
        return self.department_name
