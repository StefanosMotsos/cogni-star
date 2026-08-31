import logging

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authtoken.admin import User
from rest_framework.exceptions import ValidationError
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from api.clients.swapi_client import fetch_swapi_planets, fetch_swapi_people
from api.models import Planet, Person
from api.v1.filters import PersonFilter
from api.v1.pagination import SmallSetPagination
from api.v1.permissions import IsOwnerOrAdmin
from api.v1.serializers import PlanetSerializer, PersonSerializer, UserSerializer

logger = logging.getLogger(__name__)

class PlanetViewSet(ModelViewSet):
    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer
    pagination_class = SmallSetPagination

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAuthenticated, IsAdminUser]
        return [permission() for permission in permission_classes]

class PersonViewSet(ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    pagination_class = SmallSetPagination

    filter_backends = [DjangoFilterBackend]
    filterset_class = PersonFilter

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAuthenticated, IsAdminUser]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        if serializer.validated_data['homeworld'] is None:
            raise ValidationError("person must have a homeworld")
        serializer.save()

class UserDetailsAPIView(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]

    def get_object(self):
        return self.request.user

class PopulateView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def post(self, request):
        planets_data = fetch_swapi_planets()
        url_to_planet = {}

        for item in planets_data:
            planet = Planet.objects.create(
                name=item['name'],
                rotation_period=item['rotation_period'],
                orbital_period=item['orbital_period'],
                diameter=item['diameter'],
                climate=item['climate'],
                gravity=item['gravity'],
                terrain=item['terrain'],
                surface_water=item['surface_water'],
                population=item['population'],
            )
            url_to_planet[item['url']] = planet

        people_data = fetch_swapi_people()

        for item in people_data:
            Person.objects.create(
                name=item['name'],
                height=item['height'],
                mass=item['mass'],
                hair_color=item['hair_color'],
                skin_color=item['skin_color'],
                eye_color=item['eye_color'],
                birth_year=item['birth_year'],
                gender=item['gender'],
                homeworld=url_to_planet.get(item['homeworld']),
            )

        logger.info("Populated %d planets and %d people from SWAPI", len(planets_data), len(people_data))

        return Response({
            "planets_created": len(planets_data),
            "people_created": len(people_data),
        })
