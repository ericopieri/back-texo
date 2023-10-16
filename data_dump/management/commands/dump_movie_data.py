from django.core.management.base import BaseCommand

from core.models import Movie, Studio, Producer

import csv


class Command(BaseCommand):
    help = 'Dump data from movielist.csv'

    def handle(self, *args, **kwargs):
        with open('movielist.csv', 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=';')
            for movie_data in reader:
                studio_list = movie_data['studios'].split(',')
                producer_list = movie_data['producers'].split(',')

                studio_object_list = []
                for studio in studio_list:
                    studio = Studio.objects.get_or_create(name=studio.strip())[0]
                    studio_object_list.append(studio)
                
                producer_object_list = []
                for producer in producer_list:
                    producer = Producer.objects.get_or_create(name=producer.strip())[0]
                    producer_object_list.append(producer)

                movie = Movie.objects.create(title=movie_data['title'], year=movie_data['year'])

                if movie_data['winner'] == 'yes':
                    movie.winner = True

                movie.studios.set(studio_object_list)
                movie.producers.set(producer_object_list)

                movie.save()

