from rest_framework import viewsets
from .models import Artist, Album, Song, Lyric
from .serializers import ArtistSerializer, AlbumSerializer, SongSerializer, SongWithLyricsSerializer, AlbumWithSongsSerializer


class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class SongWithLyricsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongWithLyricsSerializer


class AlbumWithSongsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumWithSongsSerializer
