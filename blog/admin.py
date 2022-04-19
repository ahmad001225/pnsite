from django.contrib import admin
from .models import Post, Category, Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    django_summernote = ('content',)
    date_hierarchy = ('published_date')
    empty_value_display = 'empty'
    list_filter = ('title', 'content','created_date' ,'published_date')
    summernote_fields = '__all__'


class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = 'empty'
    list_display=('name','post','approved')
    list_filter = ('post', 'approved', 'created_date')



admin.site.register (Category)
admin.site.register (Comment,CommentAdmin)
