from django.shortcuts import render
from blog.models import BlogAuthor, BlogPost, Comment
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from blog.forms import MakeComment
from django.urls import reverse
import datetime


# Create your views here.

class BlogPostListView(generic.ListView):
    model = BlogPost

class BlogPostDetailView(generic.DetailView):
    model = BlogPost

class BlogAuthorListView(generic.ListView):
    model = BlogAuthor

class BlogAuthorDetailView(generic.DetailView):
    model = BlogAuthor

@login_required
def make_comment(request, pk):
    """View function for making a comment."""
    target_blog = get_object_or_404(BlogPost, pk=pk)

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = MakeComment(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            new_comment = Comment()
            new_comment.content = form.cleaned_data['new_comment']
            new_comment.target_blog_post = target_blog
            new_comment.user = request.user
            new_comment.post_date = datetime.date.today()
            new_comment.save()

            # redirect to a new URL:
            return HttpResponseRedirect(f'/blog/blog/{pk}')

    # If this is a GET (or any other method) create the default form.
    else:
        # proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = MakeComment()

    context = {
        'form': form,
    }

    return render(request, 'blog/make_comment.html', context)