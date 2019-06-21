from django.contrib import admin

# Register your models here.
from blog.models import BlogAuthor, BlogPost, Comment

admin.site.register(BlogAuthor)
admin.site.register(BlogPost)
admin.site.register(Comment)
