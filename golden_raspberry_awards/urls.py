from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from core.views import MovieViewSet, StudioViewSet, ProducerViewSet

router = routers.DefaultRouter()

router.register(r"movies", MovieViewSet)
router.register(r"studios", StudioViewSet)
router.register(r"producers", ProducerViewSet)

urlpatterns = [path("admin/", admin.site.urls), path("api/", include(router.urls))]
