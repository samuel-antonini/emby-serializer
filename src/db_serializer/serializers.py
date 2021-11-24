from rest_framework import serializers

from .models import EmbyMediaItem, EmbyMediaStream, EmbyMediaLinkedItem


class EmbyMediaStreamSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmbyMediaStream
        fields = '__all__'


class EmbyMediaLinkedItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmbyMediaLinkedItem
        fields = ['id', 'name']


class EmbyMovieSerializer(serializers.ModelSerializer):
    media_streams = EmbyMediaStreamSerializer(source="embymediastream_set", many=True)
    genres = EmbyMediaLinkedItemSerializer(read_only=True, many=True, source='linked_genres')
    studios = EmbyMediaLinkedItemSerializer(read_only=True, many=True, source='linked_studios')
    providers = serializers.DictField(source='provider_ids_dict')

    class Meta:
        model = EmbyMediaItem
        fields = 'id', 'original_title', 'name', 'production_year', 'genres', 'studios', 'overview', 'community_rating', \
                 'official_rating', 'critic_rating', 'providers', 'images', 'filename', 'path', 'container', \
                 'width', 'height', 'size', 'runtime_ticks', 'total_bitrate', 'date_created', 'date_modified', \
                 'media_streams'


class EmbyTvShowSerializer(serializers.ModelSerializer):
    genres = EmbyMediaLinkedItemSerializer(read_only=True, many=True, source='linked_genres')
    studios = EmbyMediaLinkedItemSerializer(read_only=True, many=True, source='linked_studios')
    providers = serializers.DictField(source='provider_ids_dict')

    class Meta:
        model = EmbyMediaItem
        fields = 'id', 'original_title', 'name', 'production_year', 'genres', 'studios', 'overview', \
                 'community_rating', 'official_rating', 'critic_rating', 'providers', 'images', 'path', \
                 'date_created', 'date_modified'


class EmbyEpisodeSerializer(serializers.ModelSerializer):
    media_streams = EmbyMediaStreamSerializer(source="embymediastream_set", many=True)
    providers = serializers.DictField(source='provider_ids_dict')
    season = serializers.ReadOnlyField(source='parent_index_number')
    episode = serializers.ReadOnlyField(source='index_number')

    class Meta:
        model = EmbyMediaItem
        fields = 'id', 'original_title', 'production_year', 'series_name', 'season', 'episode', 'name', \
                 'overview', 'community_rating', 'official_rating', 'critic_rating', 'providers', 'images', \
                 'filename', 'path', 'container', 'width', 'height', 'size', 'runtime_ticks', 'total_bitrate', \
                 'date_created', 'date_modified', 'media_streams'
