from rest_framework.viewsets import ModelViewSet

from core.models import Producer
from core.serializers import ProducerSerializer


class ProducerViewSet(ModelViewSet):
    queryset = Producer.objects.all()
    serializer_class = ProducerSerializer
