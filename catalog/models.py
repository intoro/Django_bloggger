from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Genre(models.Model):
    """
    Model representing a book genre (e.g. Science Fiction, Non Fiction).
    """
    name = models.CharField(max_length=200, help_text="Enter a article genre (e.g. Science Fiction, Action, Drama etc.)")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name

class Actor(models.Model):
    """
    Model representing an Actor (e.g. Tom Cruise, Daniel Radcliffe).
    """
    name = models.CharField(max_length=200, help_text="Enter a article Actors Name (e.g. Tom Cruise, Daniel Radcliff).")
    last_name = models.CharField(max_length=100)
    bio = models.TextField(max_length=1000, default='No Bio Information Set', help_text="Enter a brief Character Bio or Resume")

    def get_absolute_url(self):
        """
        Returns the url to access a particular author instance.
        """
        return reverse('actor-detail', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s %s' % (self.name, self.last_name)

from django.core.urlresolvers import reverse #Used to generate URLs by reversing the URL patterns

# -------Article------------------------------------------------------------------
# -------------------------------------------------------------------------
# -------------------------------------------------------------------------
# -------------------------------------------------------------------------
class Article(models.Model):
    """
    Model representing a book (but not a specific copy of a book).
    """
    title = models.CharField(max_length=200, null=True)
    release_date = models.DateField(null=True, blank=True)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    # Foreign Key used because book can only have one author, but authors can have multiple books
    # Author as a string rather than object because it hasn't been declared yet in the file.
    poster_one = models.CharField('Image URL 1',max_length=1000, help_text="Enter a URL to the main image of the article", null=True)
    summary_one = models.TextField(max_length=1000, help_text="Enter a brief description of the article, NO SPOILERS", null=True)
    summary_two = models.TextField(max_length=1000, null=True, blank=True, help_text="Any related facts or trivia relating to this article")
    summary_three = models.TextField(max_length=1000, null=True, blank=True, help_text="Any related facts or trivia relating to this article")
    summary_four = models.TextField(max_length=1000, null=True, blank=True, help_text="Any related facts or trivia relating to this article")
    poster_two = models.CharField('Image URL 1',max_length=1000, help_text="Enter a URL to the main image of the article", null=True)
    poster_three = models.CharField('Image URL 1',max_length=1000, help_text="Enter a URL to the main image of the article", null=True)
    poster_four = models.CharField('Image URL 1',max_length=1000, help_text="Enter a URL to the main image of the article", null=True)
    youtubeid = models.CharField('Youtube ID', max_length=1000, null=True, blank=True, help_text='Unique youtube video id for the trailer <a href="https://www.isbn-international.org/content/what-isbn">Youtube ID</a>')
    video_id = models.CharField('Video URL', max_length=1000, null=True, blank=True, help_text='Unique youtube video id for the trailer <a href="https://www.isbn-international.org/content/what-isbn">Youtube ID</a>')
    genre = models.ManyToManyField(Genre, help_text="Select a genre for this article")
    # actor = models.ManyToManyField(Actor, help_text="Select an actor for this article")
    # ManyToManyField used because genre can contain many books. Books can cover many genres.
    # Genre class has already been defined so we can specify the object above.

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.title


    def get_absolute_url(self):
        """
        Returns the url to access a particular article instance.
        """
        return reverse('article-detail', args=[str(self.id)])

    def display_genre(self):
        """
        Creates a string for the Genre. This is required to display genre in Admin.
        """
        return ', '.join([ genre.name for genre in self.genre.all()[:3] ])
    display_genre.short_description = 'Genre'

    def display_actors(self):
        """
        Creates a string for the Cast.
        """
        return ', '.join([ actor.name for actor in self.actor.all()[:3] ])
    display_actors.short_description = 'Cast'


class Author(models.Model):
    """
    Model representing an author.
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    bio = models.TextField(max_length=1000, help_text="Enter a brief description ", null=True)

    def get_absolute_url(self):
        """
        Returns the url to access a particular author instance.
        """
        return reverse('author-detail', args=[str(self.id)])


    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s %s' % (self.first_name, self.last_name)

    def display_full_name(self):
            """
            Creates a string for the name of this author.
            """
            return ' '.join([ self.first_name, self.last_name ])
    display_full_name.short_description = 'Name'

class Character(models.Model):
    """
    Model representing an author.
    """
    actor = models.ForeignKey(Actor, related_name='films')
    article = models.ForeignKey(Article, related_name='actors')
    character = models.CharField(max_length=255)

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s (%s - played by %s)' % (self.character, self.article, self.actor)
