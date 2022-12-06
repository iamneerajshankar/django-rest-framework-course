from django.contrib import admin
from myApp.models import UserInfoModel


@admin.register(UserInfoModel)
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'profession', 'job_location', 'area_pin', 'date_of_birth']
