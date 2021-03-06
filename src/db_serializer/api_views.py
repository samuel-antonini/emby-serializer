import datetime
import subprocess

import pytz
from django.conf import settings
from rest_framework import generics, filters

from .models import EmbyMediaItem, EmbyLastDatabaseCheck
from .serializers import EmbyMovieSerializer, EmbyTvShowSerializer, EmbyEpisodeSerializer


def copy_emby_database():
    base_dir = settings.BASE_DIR
    copy_database = f'cp {base_dir}/data/emby/library.db /tmp/'
    return subprocess.check_output(copy_database, shell=True, stderr=subprocess.STDOUT)


def copy_database_or_pass():
    project_timezone = settings.TIME_ZONE
    tz_fixed = pytz.timezone(project_timezone)
    check = EmbyLastDatabaseCheck.objects.last()
    if check:
        now = tz_fixed.localize(datetime.datetime.now())

        if now > check.threshold:
            copy_emby_database()
            check.last_check = tz_fixed.localize(datetime.datetime.now())
            check.save()
    else:
        copy_emby_database()
        new_db_check = EmbyLastDatabaseCheck(last_check=datetime.datetime.now())
        new_db_check.save()


# TODO: Improve filtering on all views
class EmbyMovieView(generics.ListAPIView):
    serializer_class = EmbyMovieSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['id', 'name']
    ordering = ['id']

    def get(self, request, *args, **kwargs):
        copy_database_or_pass()
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = EmbyMediaItem.objects.using('emby').filter(type=5)
        tmdb_id = self.request.query_params.get('tmdb')
        imdb_id = self.request.query_params.get('imdb')

        if tmdb_id:
            queryset = queryset.filter(provider_ids__contains=f'tmdb={tmdb_id}')
        if imdb_id:
            queryset = queryset.filter(provider_ids__contains=f'imdb={imdb_id}')

        return queryset


class EmbyTvShowView(generics.ListAPIView):
    serializer_class = EmbyTvShowSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['id', 'name']
    ordering = ['id']

    def get(self, request, *args, **kwargs):
        copy_database_or_pass()
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = EmbyMediaItem.objects.using('emby').filter(type=6)
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
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['id', 'name']
    ordering = ['id']

    def get(self, request, *args, **kwargs):
        copy_database_or_pass()
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = EmbyMediaItem.objects.using('emby').filter(type=8)
        tmdb_id = self.request.query_params.get('tmdb')
        tvdb_id = self.request.query_params.get('tvdb')

        if tmdb_id:
            queryset = queryset.filter(provider_ids__contains=f'tmdb={tmdb_id}')
        if tvdb_id:
            queryset = queryset.filter(provider_ids__contains=f'tvdb={tvdb_id}')

        return queryset
