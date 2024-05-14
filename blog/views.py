from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required,permission_required
from datetime import datetime
from django.contrib import messages
import string
import re
import random
from .models import *

# Create your views here.

def Home(request):
    return redirect('/blog/post_list/')

def AddCategory(request):
    if request.method == "GET":
        return render(request,"add_category.html")
    if request.method == "POST":
        category = CategoryModel.objects.create(
            name = request.POST.get('name'),
        )
        category.save()
        messages.success(request,"New category is added successfully!")
        return redirect('/blog/view_category/')

def ViewCategory(request):
    category = CategoryModel.objects.all()
    return render(request,'view_category.html',{'category':category})

def EditCategory(request,category_id):
    if request.method == "GET":
        category = CategoryModel.objects.get(id = category_id)
        return render(request,'edit_category.html',{'category':category})
    if request.method == "POST":
        category = CategoryModel.objects.get(id = category_id)
        category.name = request.POST.get('name')
        category.save()
        messages.success(request,"Category is updated successfully!")
        return redirect('/blog/view_category/')
    
def DeleteCategory(request,category_id):
    category = CategoryModel.objects.get(id = category_id)
    category.delete()
    messages.error(request,"Category is deleted successfully!")
    return redirect('/blog/view_category/')

def PostCreate(request):
    if request.method == "GET":
        category = CategoryModel.objects.all()
        return render(request,'post_create.html',{"category":category})
    if request.method == "POST":
        category = CategoryModel.objects.all()
        post = PostModel.objects.create(
            title = request.POST.get('title'),
            content = request.POST.get('content'),
            category_id = request.POST.get('category'),
            created_at = datetime.now(),
        )
        post.save()
        messages.success(request,"New post is created successfully!")
        return redirect('/blog/post_list/')

def PostList(request):
    post = PostModel.objects.all().order_by('-created_at')
    return render(request,'post_list.html',{"post":post})

def PostDetail(request,post_id):
    post = PostModel.objects.get(id = post_id)
    return render(request,'post_detail.html',{"post":post})

def PostUpdate(request,post_id):
    if request.method == "GET":
        category = CategoryModel.objects.all()
        post = PostModel.objects.get(id = post_id)
        return render(request,"post_update.html",{"post":post,"category":category})
    if request.method == "POST":
        category = CategoryModel.objects.all()
        post = PostModel.objects.get(id = post_id)
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.category_id = request.POST.get('category')
        post.save()
        messages.success(request,"Post is updated successfully!")
        return redirect('/blog/post_list/')
    
def PostDelete(request,post_id):
    post = PostModel.objects.get(id = post_id)
    post.delete()
    messages.error(request,"Post is deleted successfully!")
    return redirect('/blog/post_list/')
