
from rest_framework import viewsets
from .models import Category, Blog, Comment, Like, PostView  
from .serializers import CategorySerializer, BlogSerializer, CommentSerializer, LikeSerializer
from .permissions import IsStaffOrSuperuserOrReadOnly
from rest_framework.generics import CreateAPIView, ListCreateAPIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class CreatedByModelMixin:
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class CategoryView(CreatedByModelMixin, viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = None   
    permission_classes = [IsStaffOrSuperuserOrReadOnly]

class BlogViewSet(CreatedByModelMixin, viewsets.ModelViewSet):
    serializer_class = BlogSerializer

    def get_queryset(self):
 
        queryset = Blog.objects.all().order_by('-created_date', '-id')

        author = self.request.query_params.get('author', None)
        if author is not None:
            queryset = queryset.filter(author_id=author)
        
        status = self.request.query_params.get('status', None)
        if status is not None:
            queryset = queryset.filter(status=status)
 
        return queryset
 
    def retrieve(self, request, *args, **kwargs):
 
        response = super().retrieve(request, *args, **kwargs)
 
        if request.user.is_authenticated:
 
            PostView.objects.get_or_create(user=request.user, post=self.get_object())
 
        return response
 
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        super().perform_create(serializer)   

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)
        super().perform_create(serializer)   
 
class CommentListCreateAPIView(CreatedByModelMixin, ListCreateAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
 
        queryset = Comment.objects.all()
 
        post_id = self.kwargs.get('id', None)
        if post_id is not None:
            queryset = queryset.filter(post_id=post_id)
        return queryset

    def perform_create(self, serializer):
        post_id = self.kwargs.get('id', None)
        post = get_object_or_404(Blog, id=post_id)
        serializer.save(user=self.request.user, post=post)
        super().perform_create(serializer)   

class LikeListCreateAPIView(ListCreateAPIView):
    serializer_class = LikeSerializer 
    queryset = Like.objects.all()
 
    def create(self, request, *args, **kwargs):
 
        post_id = kwargs.get('id', None)
 
        post = get_object_or_404(Blog, id=post_id)
 
        status = Like.toggle(request.user, post)
        return Response({'status': status})

