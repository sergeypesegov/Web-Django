from django.http import HttpResponse
from django.shortcuts import render
from .models import Post


# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'forum/index.html',
                  context={'posts': posts})  # по дефолту джанго ищет все рендер шаблоны в папке templates
    # в шаблон передавать КЛЮЧ словаря, то есть 'name'

def about(request):
    return render(request, 'forum/about.html')
