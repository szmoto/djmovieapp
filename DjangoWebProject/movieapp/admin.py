from django.contrib import admin

from movieapp.models import Movie

# Register your models here.


class MovieAdmin(admin.ModelAdmin):
    """Definition of the Poll editor."""

    list_display = ('title','star','language','filehd', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['title']
    date_hierarchy = 'pub_date'

admin.site.register(Movie, MovieAdmin)
