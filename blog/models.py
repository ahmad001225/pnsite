from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField (default='')
    parent = models.ForeignKey ( 'self', blank=True, null=True, related_name='children', on_delete=models.CASCADE )


    class Meta:
        unique_together = ('slug', 'parent',)
        verbose_name_plural = "categories"

    def __str__(self):
        full_path = [self.name]
        k = self.parent
        while k is not None:
            full_path.append ( k.name )
            k = k.parent
        return ' -> '.join ( full_path[::-1] )

class Comment(models.Model):
 #   post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=42)
    email = models.EmailField(max_length=75)
    website = models.URLField(max_length=200, null=True, blank=True)
    message = models.TextField()
    approved = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_date']



class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    message = RichTextField ( blank=True, null=True )
    author = models.ForeignKey ( User, on_delete=models.SET_NULL, null=True)
    image = models.ImageField ( upload_to='blog/', default='blog/default.jpg' )
    category = models.ManyToManyField(Category)
    comment = models.ManyToManyField ( Comment )
    tags=TaggableManager()
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['created_date']

    def __str__(self):
        return self.title

    def snippests(self):
        return self.content[:500]

    def count_cat(self):
        return self.category.all().count()

