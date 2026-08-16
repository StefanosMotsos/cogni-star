from rest_framework import serializers

from api.models import Person, Planet


class PlanetSerializer(serializers.ModelSerializer):

    uuid = serializers.UUIDField(read_only=True)

    class Meta:
        model = Planet
        exclude = ('id',)

class PersonSerializer(serializers.ModelSerializer):

    uuid = serializers.UUIDField(read_only=True)
    homeworld = PlanetSerializer(read_only=True)

    class Meta:
        model = Person
        exclude = ('id',)