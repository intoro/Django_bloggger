from django.contrib import admin

# Register your models here.

from .models import Actor, Genre, Article, Author, Character

# admin.site.register(article)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    list_filter = ('author', 'release_date')
    fieldsets = (
        ('Author', {
            'fields': ('author', 'genre')
        }),
        ('Meta Information', {
            'fields': ('title', 'poster_one','release_date')
        }),
        ('Extra Info', {
            'fields': ( 'summary_one', 'summary_two', 'summary_three', 'summary_four' ,'poster_two','poster_three','poster_four', 'youtubeid', 'video_id')
        }),


    )

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('display_full_name', 'date_of_birth', 'bio')
    # list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'bio')]

# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)

admin.site.register(Actor)

admin.site.register(Genre)

admin.site.register(Character)
