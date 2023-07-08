from django.contrib import admin

from .models import Blog, Category, Comment, Like, PostView
from import_export import resources
from import_export.admin import ImportExportModelAdmin

admin.site.site_title = 'CoolBlog Title'
admin.site.site_header = 'CoolBlog Header'
admin.site.index_title = 'CoolBlog Index Page'

class CommentInline(admin.TabularInline):   
    model = Comment  
    extra = 1  
    classes = ['collapse']  

class BlogModelResource(resources.ModelResource):  
    class Meta:
        model = Blog

class BlogModelAdmin(ImportExportModelAdmin):
 
    list_display = ["id", "title", "author", "category","publish_date", "status", "created_date", "updated_date"]
 
    list_editable = ["status"]
 
    list_display_links = ["id",'title']
 
    prepopulated_fields = {'slug' : ['title']}
 
    resource_class = BlogModelResource
 
    ordering = ['-created_date','-id']
 
    list_per_page = 20
 
    search_help_text = 'Arama yapmak için burayı kullanabilirsiniz.'
 
    search_fields = ['id', 'title']
 
    date_hierarchy = 'created_date'
 
    inlines = [CommentInline]
 
    def set_status_p(self, request, queryset):
        count = queryset.update(status="p")
        self.message_user(request, f'{count} adet blog "Published" olarak işaretlendi.')
 
    def set_status_d(self, request, queryset):
        count = queryset.update(status="d")
        self.message_user(request, f'{count} adet blog "Draft" olarak işaretlendi.')
 
    actions = ('set_status_p', 'set_status_d')
 
    set_status_p.short_description = 'İşaretli bloglari Published yap'
    set_status_d.short_description = 'İşaretli bloglari Draft yap'
 
    def added_days_ago(self, object):
        from django.utils import timezone
        different = timezone.now() - object.created_date
        return different.days
 
    list_display += ["added_days_ago"]
 
    def comments_count(self, object):
        count = object.blog_comments.count()
        return count
 
    list_display += ['comments_count']
 
    def likes_count(self, object):
        count = object.blog_likes.count()
        return count
 
    list_display += ['likes_count']

class CommentModelAdmin(admin.ModelAdmin):
 
    list_display = ('id', 'user', 'post', 'content', 'time_stamp', 'created_date', 'updated_date')
 
    list_filter = ('post__title',)   
 
    list_display_links = ["id",'content']
 
    date_hierarchy = 'created_date'

class LikeModelAdmin(admin.ModelAdmin):
 
    list_display = ('id', 'user', 'post', 'created_date', 'updated_date')
 
    list_filter = ('post__title',)   
 
    list_display_links = ["id",]
 
    date_hierarchy = 'created_date'

admin.site.register(Blog, BlogModelAdmin)  
admin.site.register(Category)
admin.site.register(Comment, CommentModelAdmin)
admin.site.register(Like, LikeModelAdmin)
admin.site.register(PostView)