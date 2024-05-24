
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm


#________________________________________________________________________________HOME
def home(request):
    '''
    Retrieves and renders user_
    '''
    posts = Post.objects.all().order_by('-created_on')

    context = {
        "posts": posts,
    }

    return render(request, "home.html", context)


#________________________________________________________________________________POST
@login_required  
def post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            new_post        = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            return redirect('home')
    else:
        form = PostForm()

    return render(request, "memories1/post.html", {"form": form})


