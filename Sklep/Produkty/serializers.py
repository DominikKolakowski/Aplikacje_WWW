from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import *


class ProducentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producent
        fields = ['id', 'nazwa', 'opis']


class KategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kategoria
        fields = ['id', 'nazwa']


class ProduktySerializer(serializers.ModelSerializer):
    class Meta:
        model = Produkty
        fields = ['id', 'kategoria', 'producent', 'nazwa','opis', 'ilosc', 'cena']