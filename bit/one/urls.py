from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet


app_name = 'one'

router = DefaultRouter()
router.register(r'orders', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
