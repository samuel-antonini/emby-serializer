from rest_framework import generics

from .models import EmbyMediaItem
from .serializers import EmbyMovieSerializer, EmbySerieSerializer, EmbyEpisodeSerializer


# TODO: Improve filtering on all views
class EmbyMovieView(generics.ListAPIView):
    serializer_class = EmbyMovieSerializer

    def get_queryset(self):
        queryset = EmbyMediaItem.objects.using('emby').filter(type=5).order_by('id')
        tmdb_id = self.request.query_params.get('tmdb')
        imdb_id = self.request.query_params.get('imdb')

        if tmdb_id:
            queryset = queryset.filter(provider_ids__contains=f'tmdb={tmdb_id}')
        if imdb_id:
            queryset = queryset.filter(provider_ids__contains=f'imdb={imdb_id}')

        return queryset


class EmbySeriesView(generics.ListAPIView):
    serializer_class = EmbySerieSerializer

    def get_queryset(self):
        queryset = EmbyMediaItem.objects.using('emby').filter(type=6).order_by('id')
        imdb_id = self.request.query_params.get('imdb')
        tmdb_id = self.request.query_params.get('tmdb')
        tvdb_id = self.request.query_params.get('tvdb')

        if imdb_id:
            queryset = queryset.filter(provider_ids__contains=f'imdb={imdb_id}')
        if tmdb_id:
            queryset = queryset.filter(provider_ids__contains=f'tmdb={tmdb_id}')
        if tvdb_id:
            queryset = queryset.filter(provider_ids__contains=f'tvdb={tvdb_id}')

        return queryset


class EmbyEpisodesView(generics.ListAPIView):
    serializer_class = EmbyEpisodeSerializer

    def get_queryset(self):
        queryset = EmbyMediaItem.objects.using('emby').filter(type=8).order_by('id')
        tmdb_id = self.request.query_params.get('tmdb')
        tvdb_id = self.request.query_params.get('tvdb')

        if tmdb_id:
            queryset = queryset.filter(provider_ids__contains=f'tmdb={tmdb_id}')
        if tvdb_id:
            queryset = queryset.filter(provider_ids__contains=f'tvdb={tvdb_id}')

        return queryset
