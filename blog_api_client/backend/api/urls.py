from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryView, BlogViewSet, CommentListCreateAPIView, LikeListCreateAPIView

router = DefaultRouter()
router.register('categories', CategoryView, basename='category')
router.register('blogs', BlogViewSet, basename='blog')
 
urlpatterns = [
    path('likes/<int:id>/', LikeListCreateAPIView.as_view(), name='like'),
    path('comments/<int:id>/', CommentListCreateAPIView.as_view(), name='comment'),
    path('', include(router.urls)),
]

'''
from django.shortcuts import redirect

def some_view(request):
 
    return redirect('like', id=5)   
'''