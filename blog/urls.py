"""my_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import *

urlpatterns = [
    path('view_category/',ViewCategory),
    path('add_category/',AddCategory),
    path('edit_category/<int:category_id>/',EditCategory),
    path('delete_category/<int:category_id>/',DeleteCategory),
    path('post_list/',PostList),
    path('post_create/',PostCreate),
    path('post_detail/<int:post_id>/',PostDetail),
    path('post_update/<int:post_id>/',PostUpdate),
    path('post_delete/<int:post_id>/',PostDelete),
]
