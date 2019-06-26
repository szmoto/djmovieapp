from django.contrib import admin

from movieapp.models import Movie

# Register your models here.


class MovieAdmin(admin.ModelAdmin):
    """Definition of the Poll editor."""

    list_display = ('id','title','star','language','is_mv', 'pub_date')
    list_filter = ['mvtype']
    search_fields = ['title']
    list_per_page = 15
    ordering = ('id',)
    date_hierarchy = 'pub_date'

admin.site.register(Movie, MovieAdmin)
