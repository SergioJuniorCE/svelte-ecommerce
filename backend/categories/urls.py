from django.urls import include, path
from rest_framework import routers

from .views import CategoryViewset

router = routers.DefaultRouter()
router.register('', CategoryViewset)

urlpatterns = [
  path('', include(router.urls)),
]