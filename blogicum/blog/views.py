from django.shortcuts import render, get_object_or_404

from .models import Post, Category

POST_NUM = 5


def index(request):
    """Главная страница."""
    template = 'blog/index.html'
    post_list = Post.objects.pub_filter().category_filter()[:POST_NUM]
    context = {'post_list': post_list}
    return render(request, template, context)


def post_detail(request, id):
    """Отдельная публикация."""
    template = 'blog/detail.html'
    post = get_object_or_404(
        Post.objects.pub_filter().category_filter(),
        pk=id
    )
    context = {'post': post}
    return render(request, template, context)


def category_posts(request, category_slug):
    """Категория публикаций."""
    template = 'blog/category.html'
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    post_list = category.posts.pub_filter()
    context = {
        'category': category,
        'post_list': post_list}
    return render(request, template, context)
