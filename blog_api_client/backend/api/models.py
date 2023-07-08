from django.db import models

from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class FixModel(models.Model):
 
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Category(FixModel):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name
 
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

class Blog(FixModel):
 
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=3000)
    image = models.URLField(max_length=400)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name='category_blogs')
    publish_date = models.DateTimeField(auto_now_add=True, editable=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_blogs')
    STATUS_CHOICES = [
        ('d', 'Draft'),
        ('p', 'Published'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='d')
 
    slug = models.SlugField(
        max_length=50,
        validators=[
            RegexValidator(
                regex=r'^[-a-zA-Z0-9_]+$',
                message='Slug can only contain alphanumeric characters, hyphens, and underscores.'
            )
        ],
        null=True, 
        blank=True,
    )
 
    def __str__(self):
        return self.title
 
    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"
        
class Comment(FixModel):
 
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comments')
    post = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='blog_comments')
    content = models.TextField()
    time_stamp = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return f'Comment by {self.user} on {self.post}'
 
    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

class Like(FixModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_likes')
    post = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='blog_likes')

    def __str__(self):
        return f'Like by {self.user} on {self.post}'
 
    class Meta:
        verbose_name = "Like"
        verbose_name_plural = "Likes"
 
    @classmethod
    def toggle(cls, user, post):
 
        obj, created = cls.objects.get_or_create(user=user, post=post)  
 
        if not created:
          obj.delete()
          return False  
 
        else:
          obj.created_by = user
          obj.save()
          return True  
 
class PostView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_views')
    post = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='blog_views')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Viewed by {self.user} on {self.post}'
 
    class Meta:
        verbose_name = "Post View"
        verbose_name_plural = "Post Views"
        unique_together = (('user', 'post'),)