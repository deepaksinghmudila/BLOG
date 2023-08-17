from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def blogHome(request):
    return render(request, 'blog/blogHome.html')
    # return HttpResponse('BlogApp BlogHome Page! We will keep all the blog posts here...')

def blogPost(request, slug):
    return render(request, 'blog/blogPost.html')
    # return HttpResponse(f'BlogPost Page! {slug}')