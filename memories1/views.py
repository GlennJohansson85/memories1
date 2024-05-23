from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from blog_app.models import Post
from .forms import PostForm, CommentForm, PostDeleteForm
import logging

# home.html
def home(request):
    # Order posts by 'created_on' in descending order
    posts = Post.objects.all().order_by('-created_on')
    delete_form = PostDeleteForm()

    if request.method == 'POST':
        if 'delete' in request.POST:
            post_id_to_delete = request.POST.get('post_id_to_delete')
            post_instance = get_object_or_404(Post, id=post_id_to_delete)
            post_instance.delete_post()
            return redirect('home')

    context = {
        "posts": posts,
        "delete_form": delete_form,
    }

    return render(request, "blog_app/home.html", context)


def post_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by("-created_on")
    context = {
        "category": category,
        "posts": posts,
    }
    return render(request, "blog_app/post_category.html", context)


@login_required  
def post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user  
            new_post.save()
            return redirect('home')
    else:
        form = PostForm()

    return render(request, "blog_app/post.html", {"form": form})

print("Comment view called!")
logger = logging.getLogger(__name__)


@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    # Check if the logged-in user is the owner of the post
    if request.user == post.user:
        post.delete()

    return redirect('home')


print("Comment view called!")

logger = logging.getLogger(__name__)


@login_required
def comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            try:
                comment = form.save(user=request.user, post=post, commit=True)
                # Rest of your code
            except Exception as e:
                logger.error(f"Error saving comment: {e}")
        else:
            logger.error(f"Invalid form: {form.errors}")
            logger.error(f"Form data: {request.POST}") # debugging
    else:
        form = CommentForm()

    return render(request, 'blog_app/home.html', {'post': post, 'form': form})