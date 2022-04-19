from django.urls import include, path
from blog import views
app_name="blog"
urlpatterns = [
    path('', views.blog_view, name='index'),
    path('single/<int:pid>', views.blog_single, name='single'),
    path ( "search/", views.blog_search, name='search' ),
    path ( "category<str:cat_name>", views.blog_view, name='category' ),
    path ( "tag/<str:tag_name>", views.blog_view, name='tag' ),
    path ( "author<str:author_name>", views.blog_view, name='author' ),

]