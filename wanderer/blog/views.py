from django.shortcuts import render

posts = [
    {
        'author': 'Dilain',
        'title': 'blog 1',
        'content': 'this is the first blog',
        'date_posted': 'January 5, 2020'
    },
    {
        'author': 'Gunasekara',
        'title': 'blog 2',
        'content': 'this is the second blog',
        'date_posted': 'January 6, 2020'
    }

]


def index(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)
