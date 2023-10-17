from rest_framework.serializers import ModelSerializer

from core.models import Studio


class StudioSerializer(ModelSerializer):
    class Meta:
        model = Studio
        fields = "__all__"
