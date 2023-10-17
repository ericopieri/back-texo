from rest_framework.viewsets import ModelViewSet

from core.models import Studio
from core.serializers import StudioSerializer


class StudioViewSet(ModelViewSet):
    queryset = Studio.objects.all()
    serializer_class = StudioSerializer
