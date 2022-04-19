"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls import  include
from django.conf.urls.static import static
from website.sitemaps import StaticViewSitemap
from blog.sitemaps import BlogSiteMap
from django.contrib.sitemaps.views import sitemap
from django.contrib.auth.views import LogoutView
from blog import views

sitemaps={
    'static':StaticViewSitemap,
    'blog': BlogSiteMap,
}

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path('accounts/', include('allauth.urls' ) ),
    path('logout', LogoutView.as_view()),
    path("", include("website.urls")),
    path ( 'blog/', include ( 'blog.urls' ) ),
    path ( 'sitemap.xml', sitemap, {'sitemaps': sitemaps},name='django.contrib.sitemaps.views.sitemap'),
    path ( 'robot.txt', include ( 'robots.urls' ) ),
    path ( '__debug__/', include ( 'debug_toolbar.urls' ) ),
    path ( 'captcha/', include ( 'captcha.urls' ), name='captcha' ),
    path ( 'summernote/', include ( 'django_summernote.urls' ) ),
    path ( 'api/posts', views.PostList.as_view () ),
    path ( 'api/posts/<int:pk>', views.PostDetail.as_view () ),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
