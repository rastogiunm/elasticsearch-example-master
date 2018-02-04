from django.conf.urls import url, include
from . import views

from django.views.generic import ListView, DetailView
from elasticsearchapp.models import BlogPost

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^edit/$', ListView.as_view(queryset=BlogPost.objects.all().order_by("-posted_date")[:25],
                                    template_name="elasticsearchapp/blogposts.html")),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^search/', views.search, name='search'),
]