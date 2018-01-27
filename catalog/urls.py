from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^articles/$', views.ArticleListView.as_view(), name='articles'),
    url(r'^article/(?P<pk>\d+)$', views.ArticleDetailView.as_view(), name='article-detail'),
    url(r'^authors/$', views.AuthorListView.as_view(), name='authors'),
    url(r'^author/(?P<pk>\d+)$', views.AuthorDetailView.as_view(), name='author-detail'),
    url(r'^actors/$', views.ActorListView.as_view(), name='actors'),
    url(r'^actor/(?P<pk>\d+)$', views.ActorDetailView.as_view(), name='actor-detail'),
]
