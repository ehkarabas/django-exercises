from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArtistViewSet, AlbumViewSet, SongViewSet, SongWithLyricsViewSet, AlbumWithSongsViewSet

router = DefaultRouter()
router.register(r'artists', ArtistViewSet)
router.register(r'albums', AlbumViewSet)
router.register(r'songs', SongViewSet)
router.register(r'songs_with_lyrics', SongWithLyricsViewSet,
                basename='songs_with_lyrics')
router.register(r'albums_with_songs', AlbumWithSongsViewSet,
                basename='albums_with_songs')

urlpatterns = [
    path('', include(router.urls)),
]
