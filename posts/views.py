from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Post , Comment
from django.contrib.auth.decorators import login_required
from .forms import PostForm, CommentForm


def post_list(request):
    categories = Category.objects.all()
    posts = Post.objects.all()
    return render(request, 'posts/post_list.html', {
        'categories': categories,
        'posts': posts
    })

def category_posts(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    posts = Post.objects.filter(category=category)
    return render(request, 'posts/category_detail.html', {
        'category': category,
        'posts': posts
    })


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    form = CommentForm(request.POST)

    return render(request, 'posts/post_detail.html', {'post': post, "form": form})



"""
post
get

"""

@login_required
def create_post(request):
    if request.method == 'POST':
        #print("request data", request.POST['title'], request.POST['description'], request.POST['category'])
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user   
            post.save()
            return redirect('posts:post_list')
    else:
        form = PostForm()

    return render(request, 'posts/create_post.html', {'form': form})



@login_required
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if post.author != request.user:
        return redirect('posts:post_list')

    post.delete()
    return redirect('posts:post_list')


@login_required
def update_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if post.author != request.user:
            return redirect('posts:post_list')
        if form.is_valid():
            form.save()
            return redirect('posts:post_detail', post_id=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'posts/update_post.html', {'form': form})




def post_list(request):
    query = request.GET.get('q')  # получаем текст из поиска
    if query:
        posts = Post.objects.filter(title__icontains=query)  # ищем в заголовке
    else:
        posts = Post.objects.all()
    return render(request, 'posts/post_list.html', {'posts': posts})



@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('posts:post_detail', post_id=post.pk)
    else:
        form = CommentForm()

    return render(request, 'posts/post_detail.html', {'post': post, 'form': form})



@login_required
def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)

    if comment.author != request.user:
        return redirect('posts:post_detail', post_id=comment.post.pk)

    comment.delete()

    return redirect('posts:post_detail', post_id=comment.post.pk)





