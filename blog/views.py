from django.shortcuts import render
from .models import Post, Author, Comment

def index_view(request):
	posts = Post.objects.order_by('-created_date')[:10]
	context = {'posts': posts}
	return render(request, "blog/index.html", context)
	
def post_view(request, post_id):
	post = Post.objects.get(pk=post_id)
	comments = post.comments.order_by("-created_date")
	context = {'comments': comments, 'post': post}
	return render(request, "blog/post.html", context)
	