from email.policy import default

from django.db import models
import uuid


# Create your models here.


class Planet(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=100)
    rotation_period = models.CharField(max_length=50)
    orbital_period = models.CharField(max_length=50)
    diameter = models.CharField(max_length=50)
    climate = models.CharField(max_length=50)
    gravity = models.CharField(max_length=50)
    terrain = models.CharField(max_length=50)
    surface_water = models.CharField(max_length=50)
    population = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Person(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=100)
    height = models.CharField(max_length=100)
    mass = models.CharField(max_length=100)
    hair_color = models.CharField(max_length=50)
    skin_color = models.CharField(max_length=50)
    eye_color = models.CharField(max_length=50)
    birth_year = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    homeworld = models.ForeignKey(Planet, on_delete=models.SET_NULL, null=True, related_name='residents')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name