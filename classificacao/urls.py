from django.urls import include, path
from django.contrib import admin
from rest_framework import routers
from classificacao.filmes_series import views

router = routers.DefaultRouter()
router.register(r'filmes', views.FilmesViewSet)
router.register(r'series', views.SeriesViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
