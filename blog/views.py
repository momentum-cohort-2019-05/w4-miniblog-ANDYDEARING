from django.shortcuts import render
from blog.models import BlogAuthor, BlogPost, Comment
from django.views import generic

# Create your views here.
# def BlogListView(request):
#     """View function for home page of site."""
    
#     context = {
        
#     }

#     # Render the HTML template index.html with the data in the context variable
#     return render(request, 'index.html', context=context)

class BlogPostListView(generic.ListView):
    model = BlogPost

class BlogPostDetailView(generic.DetailView):
    model = BlogPost

class BlogAuthorListView(generic.ListView):
    model = BlogAuthor

class BlogAuthorDetailView(generic.DetailView):
    model = BlogAuthor