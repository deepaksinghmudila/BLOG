from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def blogHome(request):
    return HttpResponse('BlogApp BlogHome Page! We will keep all the blog posts here...')

def blogPost(request, slug):
    return HttpResponse(f'BlogPost Page! {slug}')