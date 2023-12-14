
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from .forms import BlogPostForm, CommentForm
from .models import BlogPost, Comment


def home(request):
    posts = BlogPost.objects.order_by('-date_added')
    return render(request, 'blogs/home.html', {'posts': posts })
@login_required
def create_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            form.save()
            return redirect('blogs:home')
    else:
        form = BlogPostForm()
    return render(request, 'blogs/create_post.html', {'form': form})
@login_required
def edit_post(request, post_id):
    post = get_object_or_404(BlogPost, pk=post_id)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blogs:home')
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'blogs/edit_post.html', {'form': form, 'post': post})
@login_required
def view_post(request, post_id):
    user = request.user
    post = get_object_or_404(BlogPost, pk=post_id)
    comments = Comment.objects.filter(post=post)

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():

            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('blogs:home')
    else:
        comment_form = CommentForm()

    return render(request, 'blogs/view_post.html', {'post': post, 'comments': comments, 'comment_form': comment_form})
@login_required
def like_post(request, post_id):
    post = BlogPost.objects.get(id=post_id)
    # Проверяем, поставил ли пользователь дизлайк ранее, и если да, то удаляем дизлайк.
    if request.user in post.dislikes.all():
        post.dislikes.remove(request.user)

    # Если пользователь уже поставил лайк, не делаем ничего.
    if request.user not in post.likes.all():
        post.likes.add(request.user)

    return redirect('blogs:home')
@login_required
def dislike_post(request, post_id):
    post = BlogPost.objects.get(id=post_id)
    # Проверяем, поставил ли пользователь лайк ранее, и если да, то удаляем лайк.
    if request.user in post.likes.all():
        post.likes.remove(request.user)

    # Если пользователь уже поставил дизлайк, не делаем ничего.
    if request.user not in post.dislikes.all():
        post.dislikes.add(request.user)

    return redirect('blogs:home')
def user_logout(request):
    logout(request)
    return redirect('blogs:home')