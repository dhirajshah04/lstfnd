from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required


@login_required()
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'lostfound/post_new.html', {'form': form})

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'lostfound/post_list.html', {'posts':posts})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                             published_date__year=year,
                             published_date__month=month,
                             published_date__day=day)
    return render(request, 'lostfound/post_detail.html', {'post': post})

@login_required()
def dashboard(request):
    return render(request, 'cadmin/dashboard.html', {})