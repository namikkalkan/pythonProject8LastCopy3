from django.contrib.sitemaps import Sitemap
from .models import *


class ArticleSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return Test.objects.all()




