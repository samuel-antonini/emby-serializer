from django.urls import path
from . import api_views

urlpatterns = [
    path('embymovies/', api_views.EmbyMovieView.as_view()),
    path('embytvshows/', api_views.EmbyTvShowView.as_view()),
    path('embyepisodes/', api_views.EmbyEpisodesView.as_view()),
]
