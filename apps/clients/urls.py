from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'clients'

router = routers.DefaultRouter()
router.register('', views.ClientViewSet, basename='clientes')
router.register('', views.ClientSocialnetworkViewSet, basename='clientes_redessociais')

urlpatterns = [
    path('', include(router.urls) )
]
