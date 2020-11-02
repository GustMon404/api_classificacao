from .models import Filme,Serie
from rest_framework import serializers

class FilmeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Filme
        fields = '__all__'

class SerieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Serie
        fields = '__all__'