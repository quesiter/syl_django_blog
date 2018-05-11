from django.shortcuts import render
<<<<<<< HEAD
from django.http import HttpResponse
from article.models import Article

# Create your views here.
def home(request):
    return HttpResponse("Hello World, Django")

def detail(request, my_args):
    post = Article.objects.all()[int(my_args)]
    str = ("title = %s, category = %s, date_time = %s, content = %s" 
        % (post.title, post.category, post.date_time, post.content))
    return HttpResponse(str)
=======

# Create your views here.
>>>>>>> 42dfd83f9f6f09c839387cbd5d1f569a97f5373e
