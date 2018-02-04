from django.shortcuts import render, render_to_response
from elasticsearchapp.models import BlogPost
from django.views.decorators import csrf
from django.views.decorators.csrf import csrf_protect

from .search import BlogPostIndex

# Create your views here.
def index(request):
    return render(request, 'elasticsearchapp/home.html')

def edit_notused(request):
    args = {}
    args.update(csrf(request))
    args['blogposts'] = BlogPost.objects.all()
    # return render(request, 'elasticsearchapp/blogposts.html')
    return render_to_response('elasticsearchapp/blogposts.html', args)

def contact(request):
    return render(request, 'elasticsearchapp/basic.html', {'content':['You can contact me at','r.....@......com']})

def search_models_notused(request):
	if request.method == "POST":
		search_text = request.POST['search_text']
	else:
		search_text = ''
    
	blogposts = BlogPost.objects.filter(title__contains=search_text)	
	return render_to_response('elasticsearchapp/ajax_search.html',{'blogposts' : blogposts})

def search(request):
    search_text = request.POST.get("search_text")
    blogposts = BlogPostIndex.search(search_text)
    print(blogposts)

    return render_to_response('elasticsearchapp/ajax_search.html',{'blogposts' : blogposts})



