from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .models import Post, Author, Comment
from datetime import datetime
import pytz

def index_view(request):
    posts = Post.objects.order_by('-created_date')[:10]
    context = {'posts': posts}
    return render(request, "blog/index.html", context)
    
def post_view(request, post_id):
    posts = Post.objects.order_by('-created_date')[:10]
    post = Post.objects.get(pk=post_id)
    comments = post.comments.order_by("-created_date")
    context = {'comments': comments, 'post': post, 'posts': posts}
    return render(request, "blog/post.html", context)

@csrf_protect
def comment_submit(request, post_id):
    if request.method == 'POST':
        if request.POST['comment'] != '':
            text = request.POST['comment']
            no_author = Author.objects.get(pk=3)
            aware_now = pytz.utc.localize(datetime.now())
            comment = Comment.objects.create(text = text, author = no_author, created_date = aware_now)
            post = Post.objects.get(pk=post_id)
            post.comments.add(comment)
            return HttpResponseRedirect("/blog/post/%s/" % post_id)
        else:
            #send error
            return HttpResponseRedirect("/blog/post/%s/" % post_id)
    return HttpResponseNotFound("Page not found")









