from myApp.models import MoviesLibraryModel
from rest_framework import serializers


class MoviesLibrarySerializer(serializers.Serializer):
    name = serializers.CharField(help_text='Field for movie name', allow_blank=False, max_length=50)
    director = serializers.CharField(help_text='Field for movie director',
                                     allow_blank=False, max_length=50)
    year = serializers.IntegerField(help_text='Field for movie release year')
    rating = serializers.DecimalField(help_text='Field for movie IMDB rating', decimal_places=2, max_digits=6)
    franchise = serializers.CharField(allow_blank=True, max_length=50)

    def create(self, validated_data):
        return MoviesLibraryModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.director = validated_data.get('director', instance.director)
        instance.year = validated_data.get('year', instance.year)
        instance.rating = validated_data.get('rating', instance.rating)
        instance.franchise = validated_data.get('franchise', instance.franchise)

        instance.save()
        return instance

    # Field level validation
    def validate_rating(self, value):
        if value <= 5.0:
            raise serializers.ValidationError("Movie Rating too low to be added to collection")
        return value

    # Object Level Validation
    def validate(self, movie_year):
        year_of_release = movie_year.get('year')
        if year_of_release < 2000:
            raise serializers.ValidationError("Movie must be released after 2000")
        return movie_year

