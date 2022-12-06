from django.db import models

""" Model to store User Info in Database """


class UserInfoModel(models.Model):
    name = models.CharField(blank=False, max_length=50, help_text="name of the user")
    profession = models.CharField(blank=False, max_length=50, help_text="user profession")
    job_location = models.CharField(blank=True, max_length=50, help_text="location of the job")
    area_pin = models.IntegerField(max_length=7, blank=True, help_text="Area Code of the location")
    date_of_birth = models.DateField(blank=True, help_text="Birth date")
