from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseNotFound

from .models import Post, Category


def index(request):
    """Главная страница."""
    template = 'blog/index.html'
    post_list = Post.objects.to_publish().filter(
        category__is_published=True,
    ).order_by('-pub_date')[:5]
    context = {'post_list': post_list}
    return render(request, template, context)


def post_detail(request, id):
    """Отдельная публикация."""
    template = 'blog/detail.html'
    post = get_object_or_404(
        Post.objects.to_publish(),
        pk=id,
        category__is_published=True
    )
    context = {'post': post}
    if not context:
        raise HttpResponseNotFound('Страница не найдена.')
    return render(request, template, context)


def category_posts(request, category_slug):
    """Категория публикаций."""
    template = 'blog/category.html'
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    post_list = category.category_posts.to_publish()
    context = {
        'category': category,
        'post_list': post_list}
    if not context:
        raise HttpResponseNotFound('Страница не найдена.')
    return render(request, template, context)
