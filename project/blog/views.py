from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    posts = [
        {"title": "My Awesome Blog", "author": "Me"},
        {"title": "Not a Awesome Blog", "author": "you"},
    ]
    context = {"posts": posts}
    return render(request, "home.html", context)


def about(request):
    return HttpResponse("<H1>About Me!</H1>")
