import algoliasearch_django as algoliasearch
from algoliasearch_django.decorators import register
from algoliasearch_django import AlgoliaIndex

from .models import Post

# algoliasearch.register(Post)


@register(Post)
class PostIndex(AlgoliaIndex):
    fields = ('id', 'title', 'content', 'created_at')
    settings = {'searchableAttributes': ['title', 'content']}
    index_name = 'blog_posts'
