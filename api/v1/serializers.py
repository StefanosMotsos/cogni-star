from django.contrib.auth.models import User
from rest_framework import serializers

from api.models import Person, Planet


class PlanetSerializer(serializers.ModelSerializer):

    uuid = serializers.UUIDField(read_only=True)
    resident_count = serializers.SerializerMethodField()

    class Meta:
        model = Planet
        exclude = ('id',)

    def get_resident_count(self, obj):
        return obj.residents.count()

class PersonSerializer(serializers.ModelSerializer):

    uuid = serializers.UUIDField(read_only=True)
    homeworld = PlanetSerializer(read_only=True)

    class Meta:
        model = Person
        exclude = ('id',)

    def validate_height(self, value):
        if value.isdigit() and int(value) < 0:
            raise serializers.ValidationError('Height cannot be negative')
        return value

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