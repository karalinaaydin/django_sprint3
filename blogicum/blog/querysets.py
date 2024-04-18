from datetime import datetime

from django.db.models import QuerySet


class MyQuerySet(QuerySet):
    """Класс типового запроса."""

    def to_publish(self):
        """Фильтр опубликованных постов."""
        return (self.select_related('author', 'location', 'category').filter(
            is_published=True,
            pub_date__lt=datetime.now()))
