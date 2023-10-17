from rest_framework.serializers import ModelSerializer

from core.models import Producer


class ProducerSerializer(ModelSerializer):
    class Meta:
        model = Producer
        fields = "__all__"
