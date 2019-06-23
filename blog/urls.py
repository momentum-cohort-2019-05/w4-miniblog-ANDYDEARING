from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogPostListView.as_view(), name='index'),
    path('blog/<int:pk>', views.BlogPostDetailView.as_view(), name='blogpost-detail'),
    path('authors/', views.BlogAuthorListView.as_view(), name="blog-authors"),
    path('author/<int:pk>', views.BlogAuthorDetailView.as_view(), name='blog-author-detail'),
]

urlpatterns += [   
    path('blog/<int:pk>/comment/', views.make_comment, name='make-comment'),
]