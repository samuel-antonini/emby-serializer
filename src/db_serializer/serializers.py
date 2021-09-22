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

    class Meta:
        model = EmbyMediaItem
        fields = 'id', 'original_title', 'name', 'genres', 'production_year', 'studios', 'filename', 'width', 'height', 'total_bitrate', 'size', 'container', \
                 'community_rating', 'official_rating', 'overview', 'critic_rating', \
                 'path', 'provider_ids', 'data', 'images', 'media_streams'


class EmbySerieSerializer(serializers.ModelSerializer):
    genres = EmbyMediaLinkedItemSerializer(read_only=True, many=True, source='linked_genres')

    class Meta:
        model = EmbyMediaItem
        fields = 'id', 'original_title', 'name', 'genres', 'production_year', 'studios', \
                 'community_rating', 'official_rating', 'overview', 'critic_rating', \
                 'path', 'provider_ids', 'data', 'images'


class EmbyEpisodeSerializer(serializers.ModelSerializer):
    media_streams = EmbyMediaStreamSerializer(source="embymediastream_set", many=True)

    class Meta:
        model = EmbyMediaItem
        fields = 'id', 'original_title', 'name', 'production_year', 'studios', 'filename', 'width', 'height', 'total_bitrate', 'size', 'container', \
                 'community_rating', 'official_rating', 'overview', 'critic_rating', \
                 'path', 'provider_ids', 'data', 'images', 'media_streams'
