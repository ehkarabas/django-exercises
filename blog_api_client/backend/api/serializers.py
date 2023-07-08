from rest_framework import serializers
from .models import Category, Blog, Comment, Like, PostView

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = []
        read_only_fields = ('created_by', 'created_date', 'updated_date')
 
class BlogSerializer(serializers.ModelSerializer):
 
    author = serializers.SlugRelatedField(read_only=True, slug_field='username')
    comments = serializers.SerializerMethodField()  
    category_name = serializers.SerializerMethodField() 
    likes = serializers.SerializerMethodField()
    likes_n = serializers.SerializerMethodField()
    post_views = serializers.SerializerMethodField()
    comment_count = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        exclude = []
        read_only_fields = ('created_by', 'created_date', 'updated_date')
 
    def get_comments(self, obj):
        comments = obj.blog_comments.all()
        return [{"id":comment.id, "user": comment.user.username, "time_stamp":comment.time_stamp, "content":comment.content, "post":comment.post.id } for comment in comments]
 
    def get_category_name(self, obj):
        return obj.category.name

    def get_likes(self, obj):
        return obj.blog_likes.count()

    def get_likes_n(self, obj):
        likes = obj.blog_likes.all()
        return [{'id': like.id, 'user_id': like.user.id, 'post_id': like.post.id} for like in likes]

    def get_post_views(self, obj):
        return obj.blog_views.count()

    def get_comment_count(self, obj):
        return obj.blog_comments.count()
    
    def validate_category(self, value):
        # 'administration' kategorisi sadece yetkili kullanıcılar tarafından kullanılabilir
        if value.name.lower() == 'administration':
            request = self.context.get("request")
            if request and not (request.user.is_staff or request.user.is_superuser):
                raise serializers.ValidationError("Sadece yetkili kullanıcılar 'administration' kategorisini kullanabilir.")
        return value

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(read_only=True, slug_field='username')
    class Meta:
        model = Comment
        exclude = []
        read_only_fields = ('created_by', 'created_date', 'updated_date')

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        exclude = []
        read_only_fields = ('created_by', 'created_date', 'updated_date')

class PostViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostView
        exclude = []
        read_only_fields = ('created_date', 'updated_date')
