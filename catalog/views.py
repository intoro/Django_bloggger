from django.shortcuts import render
from .models import Article, Author, Actor, Genre

def index(request):
    """
    View function for home page of site.
    """
    # my_parameter = 'dan'
    # Generate counts of some of the main objects
    num_articles=Article.objects.all().count()
    num_authors=Author.objects.count()  # The 'all()' is implied by default.
    num_actors=Actor.objects.count()  # The 'all()' is implied by default.
    num_genres=Genre.objects.count()  # The 'all()' is implied by default.
    return render(
        request,
        'index.html',
        context={'num_articles':num_articles,'num_authors':num_authors, 'num_actors':num_actors, 'num_genres':num_genres   },
    )
from django.views import generic


# ----Article--------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------

class ArticleListView(generic.ListView):
    model = Article

    paginate_by = 3
    def get_queryset(self):
        # return Article.objects.filter(title__icontains='water')[:5] # get 5 Articles with the string potter in the name
        return Article.objects.all().order_by('-release_date')


    # def last_ten(self):
    #     return Article.objects.filter(since=since).order_by('-id')[:10]
        # return last_ten_in_ascending_order = reversed(last_ten)

class ArticleDetailView(generic.DetailView):
    model = Article




# ----author--------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 4
    def get_queryset(self):
        return Author.objects.all()

class AuthorDetailView(generic.DetailView):
    model = Author

# ----Actor--------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------

class ActorListView(generic.ListView):
    model = Actor
    paginate_by = 8
    def get_queryset(self):
        return Actor.objects.all()

class ActorDetailView(generic.DetailView):
    model = Actor
