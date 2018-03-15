from django_perms_iscore.main import PermUIRESTModelISCore

from .models import Article


class ArticlePermUIRESTModelISCore(PermUIRESTModelISCore):

    model = Article
