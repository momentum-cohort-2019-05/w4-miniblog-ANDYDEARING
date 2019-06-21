from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.urls import reverse

class BlogPost(models.Model):
    """Model representing a blog post."""
    title = models.CharField(max_length=200, help_text='Enter a title for the blog post')
    content = models.TextField(help_text='Enter the content for your blog post.')
    blog_author = models.ForeignKey('BlogAuthor', on_delete=models.SET_NULL,
     null=True)
    post_date = models.DateField(auto_now_add=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.title
    
    class Meta:
        ordering = [ 'post_date' ]


class Comment(models.Model):
    """Model representing a comment"""
    content = models.TextField(max_length=1000, help_text='Enter your comment (1000 chars max).')
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    target_blog_post = models.ForeignKey('BlogPost', on_delete=models.CASCADE, null=True)
    post_date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = [ 'post_date' ]

class BlogAuthor(models.Model):
    """Model representing a blog author"""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.TextField(max_length=1000, help_text='Enter a short bio.')
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    class Meta:
        ordering = [ 'last_name', 'first_name' ]

    # def get_absolute_url(self):
    #     """Returns the url to access a particular blog author instance"""
    #     return reverse('blog-author-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'
