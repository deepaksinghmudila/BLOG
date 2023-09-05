from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages

from home.models import Contact


# Create your views here.
def home(request):
    return render(request, 'home/home.html')
    # return HttpResponse('Inside Home Page!')

def about(request):
    messages.error(request, 'This is About')
    messages.success(request, 'This is About-1')
    messages.success(request, 'This is About-2')
    return render(request, 'home/about.html')

def contact(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        contact = Contact(name=name, email=email, phone=phone, content=content)
        contact.save()
        if len(name) < 2 or len(email) < 3 or len(phone) < 10 or len(content) < 4:
            messages.error(request, "Please fill the form correctly")
        else:
            contact = Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, "Your message has been successfully sent")
    return render(request, 'home/contact.html')