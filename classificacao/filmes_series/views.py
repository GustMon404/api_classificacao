from .models import *
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import FilmeSerializer, SerieSerializer


class FilmesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializer
    #permission_classes = [permissions.IsAuthenticated]


class SeriesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Serie.objects.all()
    serializer_class = SerieSerializer
    #permission_classes = [permissions.IsAuthenticated]