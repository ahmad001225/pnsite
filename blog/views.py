from django.shortcuts import render
from blog.models import Post, Comment
from blog.forms import CommentForm
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .serializers import PostSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated, AllowAny  # NOQA
from rest_framework import routers, serializers, viewsets

from django.core.paginator import Paginator

app_name="blog"

class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (AllowAny) #(IsAuthenticated,)
    http_method_names = ['get', ]

class PostDetail(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
   # permission_classes = (IsAuthenticated,)
    http_method_names = ['get', ]

def blog_view(request,**kwargs):
    posts = Post.objects.filter (status=True)
    if kwargs.get ('cat_name') != None:
        posts = posts.filter ( category__name=kwargs['cat_name'] )
    if kwargs.get ('tag_name' ) != None:
        posts = posts.filterpip(tags__name__in=kwargs['tag_name'])
    if kwargs.get ( 'author_name' ) != None:
        posts = posts.filter ( author__username=kwargs['author_name'] )
    paginator = Paginator ( posts, 3 )
    try:
        page_number = request.GET.get ( 'page' )
        posts = paginator.get_page ( page_number )
    except PageNotAnInteger:
        posts = paginator.get_page ( 1 )
    except EmptyPage:
        posts = paginator.get_page ( 1 )
    context = {'posts': posts}
    return render ( request, 'blog/blog-home-side.html', context )

def blog_single(request, pid):
    posta = Post.objects.filter ( status=1 )
    post = get_object_or_404 ( posta, pk=pid )
    comments = Comment.objects.filter ( post=post.id, approved=True ).order_by ( '-created_date' )
    if request.method =='POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message ( request, messages.SUCCESS, 'your comment submitted successfully' )
        else:
            messages.add_message ( request, messages.ERROR, 'your comment didnt submited' )
    else:
        form = CommentForm()

    context = {'post': post, 'comments': comments,'form':form}
    serializer_class = PostSerializer
    queryset = Post.objects.all ()
    return render(request, 'blog/blog-single.html', context)


def blog_search(request):
    post=Post.objects.filter(status=1)
    if request.method == 'GET':
        if s := request.GET.get('search'):
            post=post.filter(content__contains()==s)
        context={'posts':post}
        return render(request, 'blog/include/blog-home.html', context)