from rest_framework import serializers
from .models import Artist, Album, Song, Lyric


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'


class AlbumSerializer(serializers.ModelSerializer):
    # artist = serializers.StringRelatedField(many=True)
    artist = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Artist.objects.all())

    class Meta:
        model = Album
        fields = ['name', 'released', 'cover', 'artist']


class SongSerializer(serializers.ModelSerializer):
    # artist = serializers.StringRelatedField()
    artist = serializers.PrimaryKeyRelatedField(queryset=Artist.objects.all())
    # album = serializers.StringRelatedField()
    album = serializers.PrimaryKeyRelatedField(queryset=Album.objects.all())

    class Meta:
        model = Song
        fields = ['name', 'released', 'artist', 'album', 'lyric']


class LyricSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lyric
        fields = '__all__'


class SongWithLyricsSerializer(serializers.ModelSerializer):
    lyric = LyricSerializer()

    class Meta:
        model = Song
        fields = ['name', 'released', 'artist', 'album', 'lyric']


class AlbumWithSongsSerializer(serializers.ModelSerializer):
    songs = SongWithLyricsSerializer(many=True, read_only=True)
    song_count = serializers.SerializerMethodField()

    class Meta:
        model = Album
        fields = ['name', 'released', 'cover',
                  'artist', 'songs', 'song_count']

    def get_song_count(self, obj):
        return obj.songs.count()
