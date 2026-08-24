from rest_framework.authtoken.admin import User
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.viewsets import ModelViewSet
from api.models import Planet, Person
from api.v1.pagination import SmallSetPagination
from api.v1.serializers import PlanetSerializer, PersonSerializer, UserSerializer


class PlanetViewSet(ModelViewSet):
    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer
    pagination_class = SmallSetPagination

class PersonViewSet(ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    pagination_class = SmallSetPagination

class UserDetailsAPIView(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user