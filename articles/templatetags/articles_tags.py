from django.template import Library

from articles.models import Article


register = Library()


@register.inclusion_tag('articles/tags/last_articles.html')
def last_articles(data_type):
    return {
        'object_list': Article.objects.filter(
            is_active=True, data_type=data_type
        )[:5]
    }
