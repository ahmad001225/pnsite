from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from blog.models import Post

app_name='blog'

class BlogSiteMap(Sitemap):
    priority = 0.5
    changefraq = 'weekly'

    def items(self):
        return Post.objects.filter(status=True)

    def lastmod(self, obj):
        return obj.pubished_date

    def location(self, item):
        return reverse('blog:single', kwargs={'pid': item.id})
