from rest_framework import serializers

from videogames.models import Videogames , User


class VideogamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Videogames
        # fields = ['name', 'number', 'collection', 'is_backlight']
        fields = '__all__'