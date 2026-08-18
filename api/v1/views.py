from rest_framework.viewsets import ModelViewSet
from api.models import Planet, Person
from api.v1.serializers import PlanetSerializer, PersonSerializer


class PlanetViewSet(ModelViewSet):
    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer

class PersonViewSet(ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer