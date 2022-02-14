from django.shortcuts import render


def home_screen_view(request, *args, **kwargs):
    context = {}
    return render(request, 'personal/home.html', context)


def test(request, *args, **kwargs):
    context = {}
    return render(request, 'personal/test.html', context)