from rest_framework import serializers

from campeones.models import Campeon, User


class CampeonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campeon
        # fields = ['nombre', 'region', 'edad', 'es_mago']
        fields = '__all__'