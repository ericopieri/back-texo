from django.contrib import admin

from .models import Movie, Studio, Producer


admin.site.register(Movie)
admin.site.register(Studio)
admin.site.register(Producer)
