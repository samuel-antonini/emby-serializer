from django.db import models


def get_linked_items_by_type(media_item, item_type):
    linked_items = EmbyItemLink.objects.using('emby').filter(item_id=media_item).filter(type=item_type)
    id_list = [item.linked_id_id for item in linked_items]
    return EmbyMediaLinkedItem.objects.using('emby').filter(id__in=id_list)


class EmbyMediaLinkedItem(models.Model):
    id = models.IntegerField('Id', primary_key=True, db_column='Id')
    type = models.IntegerField('Type', blank=True, null=True)
    name = models.CharField(max_length=250, db_column='Name', blank=True, null=True)

    class Meta:
        db_table = 'MediaItems'
        managed = False

    def __str__(self):
        return self.id


class EmbyItemLink(models.Model):
    item_id = models.OneToOneField('EmbyMediaItem', on_delete=models.CASCADE, db_column='ItemId', primary_key=True)
    type = models.IntegerField('Type', blank=True, null=True)
    linked_id = models.ForeignKey('EmbyMediaLinkedItem', on_delete=models.CASCADE, db_column='LinkedId')

    class Meta:
        db_table = 'ItemLinks'
        managed = False

    def __str__(self):
        return self.item_id


class EmbyMediaItem(models.Model):
    id = models.IntegerField('Id', primary_key=True, db_column='Id')
    guid = models.CharField('Guid', max_length=500, blank=True, null=True)
    type = models.IntegerField('Type', blank=True, null=True)
    data = models.JSONField('Data', blank=True, null=True)
    parent_id = models.IntegerField('Parent Id', db_column='ParentId', blank=True, null=True)
    path = models.CharField('Path', max_length=500, db_column='Path', blank=True, null=True)
    start_date = models.CharField('Start Date', max_length=25, db_column='StartDate', blank=True, null=True)
    end_date = models.CharField('Start Date', max_length=25, db_column='EndDate', blank=True, null=True)
    is_movie = models.BooleanField('Is Movie', db_column='IsMovie', blank=True, null=True)
    community_rating = models.FloatField('Community Rating', db_column='CommunityRating', blank=True, null=True)
    custom_rating = models.CharField('Custom Rating', max_length=3, db_column='CustomRating', blank=True, null=True)
    index_number = models.IntegerField('Index Number', db_column='IndexNumber', blank=True, null=True)
    name = models.CharField(max_length=250, db_column='Name', blank=True, null=True)
    is_locked = models.BooleanField('Is Locked', db_column='IsLocked', blank=True, null=True)
    official_rating = models.CharField('Official Rating', max_length=3, db_column='OfficialRating', blank=True,
                                       null=True)
    media_type = models.IntegerField(db_column='MediaType', blank=True, null=True)
    overview = models.TextField(db_column='Overview', blank=True, null=True)
    parent_index_number = models.IntegerField(db_column='ParentIndexNumber', blank=True, null=True)
    premiere_date = models.CharField(max_length=25, db_column='PremiereDate', blank=True, null=True)
    production_year = models.IntegerField(db_column='ProductionYear', blank=True, null=True)
    sort_name = models.CharField(max_length=250, db_column='SortName', blank=True, null=True)
    forced_sort_name = models.CharField(max_length=250, db_column='ForcedSortName', blank=True, null=True)
    runtime_ticks = models.BigIntegerField(db_column='RunTimeTicks', blank=True, null=True)
    date_created = models.CharField(max_length=25, db_column='DateCreated', blank=True, null=True)
    date_modified = models.CharField(max_length=25, db_column='DateModified', blank=True, null=True)
    is_series = models.BooleanField(db_column='IsSeries', blank=True, null=True)
    is_repeat = models.BooleanField(db_column='IsRepeat', blank=True, null=True)
    preferred_metadata_language = models.CharField(max_length=50, db_column='PreferredMetadataLanguage', blank=True,
                                                   null=True)
    preferred_metadata_country_code = models.CharField(max_length=50, db_column='PreferredMetadataCountryCode',
                                                       blank=True, null=True)
    date_last_refreshed = models.CharField(max_length=25, db_column='DateLastRefreshed', blank=True, null=True)
    date_last_saved = models.CharField(max_length=25, db_column='DateLastSaved', blank=True, null=True)
    is_in_mixed_folder = models.BooleanField(db_column='IsInMixedFolder', blank=True, null=True)
    locked_fields = models.CharField(max_length=100, db_column='LockedFields', blank=True, null=True)
    tags = models.CharField(max_length=100, db_column='Tags', blank=True, null=True)
    is_folder = models.BooleanField(db_column='IsFolder', blank=True, null=True)
    inherited_parental_rating = models.IntegerField(db_column='InheritedParentalRatingValue', blank=True, null=True)
    unrated_type = models.IntegerField(db_column='UnratedType', blank=True, null=True)
    top_parent_id = models.IntegerField(db_column='TopParentId', blank=True, null=True)
    critic_rating = models.FloatField(db_column='CriticRating', blank=True, null=True)
    presentation_unique_key = models.CharField(max_length=25, db_column='PresentationUniqueKey', blank=True, null=True)
    original_title = models.CharField(max_length=100, db_column='OriginalTitle', blank=True, null=True)
    is_virtual_item = models.BooleanField(db_column='IsVirtualItem', blank=True, null=True)
    series_name = models.CharField(max_length=100, db_column='SeriesName', blank=True, null=True)
    album = models.CharField(max_length=100, db_column='Album', blank=True, null=True)
    album_id = models.IntegerField(db_column='AlbumId', blank=True, null=True)
    series_id = models.IntegerField(db_column='SeriesId', blank=True, null=True)
    tagline = models.CharField(max_length=50, db_column='Tagline', blank=True, null=True)
    provider_ids = models.CharField(max_length=75, db_column='ProviderIds', blank=True, null=True)
    images = models.CharField(max_length=500, db_column='Images', blank=True, null=True)
    production_locations = models.CharField(max_length=250, db_column='ProductionLocations', blank=True, null=True)
    total_bitrate = models.IntegerField(db_column='TotalBitrate', blank=True, null=True)
    extra_type = models.IntegerField(db_column='ExtraType')
    artists = models.CharField(max_length=250, db_column='Artists')
    album_artists = models.CharField(max_length=250, db_column='AlbumArtists')
    series_presentation_unique_key = models.CharField(max_length=25, db_column='SeriesPresentationUniqueKey',
                                                      blank=True, null=True)
    external_id = models.CharField(max_length=25, db_column='ExternalId', blank=True, null=True)
    owner_id = models.IntegerField(db_column='OwnerId', blank=True, null=True)
    width = models.IntegerField(db_column='Width', blank=True, null=True)
    height = models.IntegerField(db_column='Height', blank=True, null=True)
    size = models.IntegerField(db_column='Size', blank=True, null=True)
    container = models.CharField(max_length=25, db_column='Container', blank=True, null=True)
    status = models.IntegerField(db_column='Status', blank=True, null=True)
    display_order = models.IntegerField(db_column='DisplayOrder', blank=True, null=True)
    three_d_format = models.IntegerField(db_column='ThreeDFormat', blank=True, null=True)
    user_data_key_id = models.IntegerField(db_column='UserDataKeyId', blank=True, null=True)
    channel_number = models.CharField(max_length=25, db_column='ChannelNumber', blank=True, null=True)
    remote_trailers = models.CharField(max_length=100, db_column='RemoteTrailers', blank=True, null=True)
    filename = models.CharField(max_length=250, db_column='Filename', blank=True, null=True)
    sort_index_number = models.IntegerField(db_column='SortIndexNumber', blank=True, null=True)
    sort_parent_index_number = models.IntegerField(db_column='SortParentIndexNumber', blank=True, null=True)
    is_kids = models.BooleanField(db_column='IsKids')
    is_sports = models.BooleanField(db_column='IsSports')
    is_news = models.BooleanField(db_column='IsNews')
    index_number_end = models.IntegerField(db_column='IndexNumberEnd')

    class Meta:
        db_table = 'MediaItems'
        managed = False

    def __str__(self):
        return self.id

    def provider_ids_dict(self):
        providers_dict = None

        if self.provider_ids:
            providers_str = self.provider_ids.split("|")
            providers_list = [item.split("=") for item in providers_str]
            providers_dict = {item[0]: item[1] for item in providers_list}

        return providers_dict

    def linked_genres(self):
        return get_linked_items_by_type(self, 2)

    def linked_studios(self):
        return get_linked_items_by_type(self, 3)


class EmbyMediaStream(models.Model):
    item_id = models.ForeignKey(EmbyMediaItem, on_delete=models.CASCADE, db_column='ItemId')
    stream_index = models.IntegerField(primary_key=True, db_column='StreamIndex')
    stream_type = models.IntegerField(db_column='StreamType')
    codec = models.CharField(max_length=15, db_column='Codec')
    language = models.CharField(max_length=15, db_column='Language')
    channel_layout = models.CharField(max_length=15, db_column='ChannelLayout')
    profile = models.CharField(max_length=15, db_column='Profile')
    aspect_ratio = models.CharField(max_length=15, db_column='AspectRatio')
    path = models.CharField(max_length=200, db_column='Path')
    is_interlaced = models.BooleanField(db_column='IsInterlaced')
    bitrate = models.IntegerField(db_column='BitRate')
    channels = models.IntegerField(db_column='Channels')
    sample_rate = models.IntegerField(db_column='SampleRate')
    is_default = models.CharField(max_length=2, db_column='IsDefault')
    is_forced = models.CharField(max_length=2, db_column='IsForced')
    is_external = models.CharField(max_length=2, db_column='IsExternal')
    height = models.IntegerField(db_column='Height')
    width = models.IntegerField(db_column='Width')
    average_framerate = models.FloatField(db_column='AverageFrameRate')
    real_framerate = models.FloatField(db_column='RealFrameRate')
    level = models.FloatField(db_column='Level')
    pixel_format = models.CharField(max_length=25, db_column='PixelFormat')
    bit_depth = models.IntegerField(db_column='BitDepth')
    is_anamorphic = models.CharField(max_length=2, db_column='IsAnamorphic')
    ref_frames = models.IntegerField(db_column='RefFrames')
    codec_tag = models.CharField(max_length=25, db_column='CodecTag')
    comment = models.CharField(max_length=100, db_column='Comment')
    nal_length_size = models.CharField(max_length=25, db_column='NalLengthSize')
    is_avc = models.CharField(max_length=2, db_column='IsAvc')
    title = models.CharField(max_length=100, db_column='Title')
    time_base = models.CharField(max_length=75, db_column='TimeBase')
    codec_time_base = models.CharField(max_length=75, db_column='CodecTimeBase')
    color_primaries = models.CharField(max_length=75, db_column='ColorPrimaries')
    color_space = models.CharField(max_length=75, db_column='ColorSpace')
    color_transfer = models.CharField(max_length=75, db_column='ColorTransfer')
    extra_data = models.CharField(max_length=75, db_column='ExtraData')

    class Meta:
        db_table = 'MediaStreams2'
        managed = False

    def __str__(self):
        return self.item_id
