from django.urls import path
from . import api_views

urlpatterns = [
    path('embymovies/', api_views.EmbyMovieView.as_view()),
    path('embyseries/', api_views.EmbySeriesView.as_view()),
    path('embyepisodes/', api_views.EmbyEpisodesView.as_view()),
]
