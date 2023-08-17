from django.urls import path, include
from blogapp import views

urlpatterns = [
    path('', views.blogHome, name='blogHome'),
    path('<str:slug>', views.blogPost, name='blogPost')
]