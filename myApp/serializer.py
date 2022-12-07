from rest_framework import serializers
from myApp.models import UserInfoModel


class UserInfoSerializer(serializers.Serializer):
    name = serializers.CharField(allow_blank=False, max_length=50, help_text="name of the user")
    profession = serializers.CharField(allow_blank=False, max_length=50, help_text="user profession")
    job_location = serializers.CharField(allow_blank=True, max_length=50, help_text="location of the job")
    area_pin = serializers.IntegerField(help_text="Area Code of the location")
    date_of_birth = serializers.DateField(help_text="Birth date")

    def create(self, validated_data):
        return UserInfoModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.profession = validated_data.get('profession', instance.profession)
        instance.job_location = validated_data.get('job_location', instance.job_location)
        instance.area_pin = validated_data.get('area_pin', instance.area_pin)
        instance.date_of_birth = validated_data.get('date_of_birth', instance.date_of_birth)

        instance.save()
        return instance
