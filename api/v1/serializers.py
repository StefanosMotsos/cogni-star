from django.contrib.auth.models import User
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

class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ('is_staff', 'is_superuser', 'is_active', 'id', 'date_joined', 'last_login')

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        instance = super().update(instance, validated_data)
        if password:
            instance.set_password(password)
            instance.save()
        return instance