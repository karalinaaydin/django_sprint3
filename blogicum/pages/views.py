from django.shortcuts import render


def about(request):
    """Описание проекта."""
    template = 'pages/about.html'
    return render(request, template)


def rules(request):
    """Правила сайта."""
    template = 'pages/rules.html'
    return render(request, template)
