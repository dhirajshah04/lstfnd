from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm, ContactForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from lstfnd import pagination
from django.template import Context
from django.template.loader import get_template


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


@staff_member_required()
def post_edit(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_list')
    else:
        form = PostForm(instance=post)
    return render(request, 'lostfound/post_new.html', {'form':form})

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    post = pagination.pg_records(request, posts, 20)
    return render(request, 'lostfound/post_list.html', {'posts': post})


'''def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                             published_date__year=year,
                             published_date__month=month,
                             published_date__day=day)
    return render(request, 'lostfound/post_detail.html', {'post': post})'''

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'lostfound/post_detail.html', {'post':post})

@login_required()
def dashboard(request):
    return render(request, 'cadmin/dashboard.html', {})


@staff_member_required()
def dash_post_list(request):
    posts = Post.objects.filter(author=request.user).order_by('published_date').reverse()
    post = pagination.pg_records(request, posts, 10)
    return render(request, 'lostfound/dash_post_list.html', {'posts':post})

@staff_member_required()
def post_remove(request, slug):
    post = get_object_or_404(Post, slug=slug)
    post.delete()
    return redirect('dash_post_list')


def about(request):
    return render(request, 'lostfound/about.html', {})

def contact(request):
    form_class = ContactForm
    if request.method == 'POST':
        form = form_class(data=request.POST)
        if form.is_valid():
            Name = request.POST.get('Name','')
            Email = request.POST.get('Email','')
            template = get_template('lostfound/contact_template')
            Context = {
                'Name': Name,
                'Email': Email,
                'Message': Message,
            }

            content = template.render(Context)

            Email = EmailMessage(
                "New Contact Form Submission",
                content,
                "Your Website" + '',
                ['youremail@gmail.com'],
                headers = {'Reply-To':Email}
            )

            Email.send()
            messages.sucess(request, 'Message sent Successfully')
            return render(request, 'lostfound/contact.html', {'form':form_class})

    return render(request, 'lostfound/contact.html', {'form': form_class})