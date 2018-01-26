from django.contrib import admin

# Register your models here.

from .models import Actor, Genre, Movie, Director, Character

# admin.site.register(Movie)

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'director', 'display_genre')
    list_filter = ('director', 'release_date')
    fieldsets = (
        (None, {
            'fields': ('title','release_date', 'genre')
        }),
        ('Extra Info', {
            'fields': ('summary', 'trivia' , 'youtubeid')
        }),        
        ('Cast & Crew', {
            'fields': ('director', 'actor')
        }),
    )
    
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('display_full_name', 'date_of_birth', 'date_of_death')
    # list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    
# Register the admin class with the associated model
admin.site.register(Director, DirectorAdmin)

admin.site.register(Actor)

admin.site.register(Genre)

admin.site.register(Character)






