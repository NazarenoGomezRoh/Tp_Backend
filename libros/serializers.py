from rest_framework import serializers

from libros.models import Libros, User


class LibrosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libros
        # fields = ['name', 'number', 'collection', 'is_backlight']
        fields = '__all__'