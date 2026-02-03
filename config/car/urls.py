from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet, ColorViewSet, CarViewSet

router = DefaultRouter()
router.register(r'color',ColorViewSet)
router.register(r'company', CompanyViewSet)
router.register(r'car', CarViewSet)

urlpatterns = [
    path('', include(router.urls))
]