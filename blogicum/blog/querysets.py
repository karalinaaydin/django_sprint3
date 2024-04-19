from datetime import datetime

from django.db.models import QuerySet


class MyQuerySet(QuerySet):
    """Класс типового запроса."""

    def pub_filter(self):
        """Фильтр опубликованных постов."""
        return (self.select_related('author', 'location', 'category').filter(
            is_published=True,
            pub_date__lt=datetime.now()))

    def category_filter(self):
        """Фильтр опубликованых категорий."""
        return (self.pub_filter().filter(
            category__is_published=True
        ))
