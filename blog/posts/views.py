from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from .forms import PostModelForm
from .models import Post, Author
from analytics.models import View


def posts_list(request):
    all_posts = Post.objects.all()
    admins_posts = Post.objects.filter(author__user__username='Lam')
    editor_dudes_posts = Post.objects.filter(editor__user__username='Lam')
    context = {
        'all_posts': all_posts,
        'admins_posts': admins_posts,
        'editor_dudes_posts': editor_dudes_posts
    }
    messages.info(request, 'Here are all the current blog posts')
    return render(request, "posts/post_list.html", context)


# CRUD
# Create retrieve update and delete

def posts_detail(request, slug):
    unique_post = get_object_or_404(Post, slug=slug)
    view, created = View.objects.get_or_create(
        user=request.user,
        post=unique_post
    )
    if view:
        view.views_count += 1
        view.save()
    total_views = 0
    for v in unique_post.views.all():
        total_views += v.views_count
    context = {
        'post': unique_post,
        'views': total_views
    }
    messages.info(request, 'This is the specific detail view')
    return render(request, "posts/post_detail.html", context)


def posts_create(request):
    author, created = Author.objects.get_or_create(
        user=request.user,
        email=request.user.email,
        cellphone_num=894382982)
    form = PostModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.instance.author = author
        form.save()
        messages.info(request, 'Successfully created a new blog post!')
        return redirect('/posts/')

    context = {
        'form': form
    }
    return render(request, "posts/post_create.html", context)


def posts_update(request, slug):
    unique_post = get_object_or_404(Post, slug=slug)
    form = PostModelForm(request.POST or None,
                         request.FILES or None,
                         instance=unique_post)
    if form.is_valid():
        form.save()
        messages.info(request, 'Successfully updated your blog post.')
        return redirect('/posts/')

    context = {
        'form': form
    }
    return render(request, "posts/post_create.html", context)


def posts_delete(request, slug):
    unique_post = get_object_or_404(Post, slug=slug)
    unique_post.delete()
    messages.info(request, 'Successfully deleted blog post.')
    return redirect('/posts/')