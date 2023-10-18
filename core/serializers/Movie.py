from rest_framework.serializers import ModelSerializer, ListField

from core.models import Movie
from core.serializers.Studio import StudioSerializer
from core.serializers.Producer import ProducerSerializer


class MovieSerializer(ModelSerializer):
    studios = StudioSerializer(many=True)
    producers = ProducerSerializer(many=True)

    class Meta:
        model = Movie
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        representation["studios"] = [
            studio["name"] for studio in representation["studios"]
        ]
        representation["producers"] = [
            producer["name"] for producer in representation["producers"]
        ]

        return representation
