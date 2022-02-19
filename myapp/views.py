from django.shortcuts import render
from myapp.models import Blog


def myapp(request):
    blogs = Blog.objects.all()
    return render(request, 'myapp.html', {'blogs': blogs})