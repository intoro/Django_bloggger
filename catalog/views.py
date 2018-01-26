from django.shortcuts import render
from .models import Movie, Director, Actor, Genre

def index(request):
    """
    View function for home page of site.
    """
    my_parameter = 'dan'
    # Generate counts of some of the main objects
    num_movies=Movie.objects.all().count()
    num_directors=Director.objects.count()  # The 'all()' is implied by default.
    num_actors=Actor.objects.count()  # The 'all()' is implied by default.
    num_genres=Genre.objects.count()  # The 'all()' is implied by default.
    num_daniel=Actor.objects.filter(name__icontains=my_parameter) # The 'all()' is implied by default.
    
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_movies':num_movies,'num_directors':num_directors, 'num_actors':num_actors, 'num_genres':num_genres, 'num_daniel':num_daniel   },
    )
from django.views import generic

class MovieListView(generic.ListView):
    model = Movie
    
    paginate_by = 3
    def get_queryset(self):
        # return Movie.objects.filter(title__icontains='water')[:5] # get 5 Movies with the string potter in the name
        return Movie.objects.all().order_by('-release_date')
        
        
    # def last_ten(self):
    #     return Movie.objects.filter(since=since).order_by('-id')[:10]
        # return last_ten_in_ascending_order = reversed(last_ten)

class MovieDetailView(generic.DetailView):
    model = Movie
    
class DirectorListView(generic.ListView):
    model = Director
    
    paginate_by = 4
    def get_queryset(self):
        # return Movie.objects.filter(title__icontains='water')[:5] # get 5 Movies with the string potter in the name
        return Director.objects.all()
        
        
    # def last_ten(self):
    #     return Movie.objects.filter(since=since).order_by('-id')[:10]
        # return last_ten_in_ascending_order = reversed(last_ten)

class DirectorDetailView(generic.DetailView):
    model = Director

class ActorListView(generic.ListView):
    model = Actor
    paginate_by = 8
    def get_queryset(self):
        # return Movie.objects.filter(title__icontains='water')[:5] # get 5 Movies with the string potter in the name
        return Actor.objects.all()
        
        
    # def last_ten(self):
    #     return Movie.objects.filter(since=since).order_by('-id')[:10]
        # return last_ten_in_ascending_order = reversed(last_ten)

class ActorDetailView(generic.DetailView):
    model = Actor
    
    
    