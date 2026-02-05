from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import RAMViewSet, CPUViewSet, GPUViewSet, PCViewSet, ManufacturerViewSet

router = DefaultRouter()
router.register(r'cpu',CPUViewSet)
router.register(r'ram', RAMViewSet)
router.register(r'gpu', GPUViewSet)
router.register(r'pc', PCViewSet)
router.register(r'manufacturer', ManufacturerViewSet)

urlpatterns = [
    path('', include(router.urls))
]