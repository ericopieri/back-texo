from rest_framework.viewsets import ModelViewSet

from core.models import Movie
from core.serializers import MovieSerializer, CreateAndUpdateMovieSerializer


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()

    def get_serializer_class(self):
        if self.action == "create" or self.action == "update":
            return CreateAndUpdateMovieSerializer

        return MovieSerializer
