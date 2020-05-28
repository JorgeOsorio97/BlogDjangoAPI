from django.urls import include, path
from rest_framework import routers
from blog import views

router = routers.DefaultRouter()
router.register(r'entradas', views.EntradaModelViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path(r'login/', views.FakeLogin.as_view())
]