from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.


posts = [
    {
        'author': 'Ankur Satya',
        'title': 'First post',
        'content': "First post content",
        'date_posted': '5th April 2020'
    },
    {
        'author': 'Hank Schrader',
        'title': 'DEA',
        'content': "Breaking Bad",
        'date_posted': '1st April 2020'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html',{"title": "About"})