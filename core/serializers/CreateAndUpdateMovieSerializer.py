from rest_framework.serializers import ModelSerializer, ListField

from core.models import Movie, Studio, Producer


class CreateAndUpdateMovieSerializer(ModelSerializer):
    studios = ListField(write_only=True)
    producers = ListField(write_only=True)

    class Meta:
        model = Movie
        fields = "__all__"

    def create(self, validated_data):
        studio_list = validated_data.pop("studios", [])
        producer_list = validated_data.pop("producers", [])

        movie_object = Movie.objects.create(**validated_data)

        for studio in studio_list:
            studio, studio_created = Studio.objects.get_or_create(name=studio)
            movie_object.studios.add(studio)

        for producer in producer_list:
            producer, producer_created = Producer.objects.get_or_create(name=producer)
            movie_object.producers.add(producer)

        return movie_object

    def update(self, instance, validated_data):
        new_title = validated_data.get("title", instance.title)
        new_year = validated_data.get("year", instance.year)
        new_winner = validated_data.get("winner", instance.winner)

        instance.title = new_title
        instance.year = new_year
        instance.winner = new_winner

        instance.save()

        studio_list = validated_data.get("studios", [])
        producer_list = validated_data.get("producers", [])

        instance.studios.clear()
        instance.producers.clear()

        for studio in studio_list:
            studio, studio_created = Studio.objects.get_or_create(name=studio)
            instance.studios.add(studio)

        for producer in producer_list:
            producer, producer_created = Producer.objects.get_or_create(name=producer)
            instance.producers.add(producer)

        instance.save()

        return instance
