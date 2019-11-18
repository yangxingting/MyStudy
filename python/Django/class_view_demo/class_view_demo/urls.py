"""class_view_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from app_index import views
from django.views.generic import TemplateView

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.view_index),
    path('book/', views.BookListView.as_view(), name='booklist'),
    path('add_book/', views.AddBookView.as_view(), name='addbook'),
    path('bookdetail/<book_name>/', views.BookDetail.as_view(), name='bookdetail'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('aboutour/', views.view_About.as_view(), name='aboutour'),

]
