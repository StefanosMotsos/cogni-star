from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.v1.views import PersonViewSet, PlanetViewSet, UserDetailsAPIView, PopulateView

router = DefaultRouter()
router.register('people', PersonViewSet)
router.register('planets', PlanetViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('me/', UserDetailsAPIView.as_view()),
    path('populate/', PopulateView.as_view()),
]