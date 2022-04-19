from ..models import Category, Comment, Post
from django import template

register = template.Library()

@register.simple_tag(name="totalposts")  # Number published post
def function():
    return Post.objects.filter(status=1).count()


@register.simple_tag(name="posts")  # published posts
def function():
    return Post.objects.filter(status=1)

@register.simple_tag(name='comment_count')
def function(pid):
    return Comment.objects.filter(post=pid, approved=True).count()

@register.simple_tag(name='post_title')
def function(pid, req='p'):
    if req == 'n':
        pid = pid+1
    else:
        pid = pid-1
    return Post.objects.filter(id=pid, status=True).get(pk=pid)

@register.inclusion_tag('blog/blog-nav-post.html')
def navposts(pa, b, *args, **kwargs):
    post = Post.objects.filter(id=3)
    return {'post': post}

@register.filter  # posts content summery
def snippect(value, arg=20):
    return value[:arg] + '...'

@register.inclusion_tag('blog/include/blog-posts.html')
def latestposts():
    posts = Post.objects.filter(status=1).order_by('published_date')[:5]
    return {'posts': posts}


@register.inclusion_tag('blog/include/blog-category.html')
def postcategories():
    posts = Post.objects.filter(status=True)
    return {'posts': posts}

@register.inclusion_tag('blog/include/blog-tag.html')
def posttags():
    posts = Post.objects.filter(status=True)
    return {'posts': posts}

@register.inclusion_tag('blog/include/blog-related.html')
def postrelated():
    posts = Post.objects.filter(status=True)
    return {'posts': posts}




