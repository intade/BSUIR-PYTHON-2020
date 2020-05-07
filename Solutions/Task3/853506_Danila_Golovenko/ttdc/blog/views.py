from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post 
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import PostForm, CommentForm
from django.template.defaultfilters import slugify

# Create your views here.

def post_list(request):
    object_list = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    paginator = Paginator(object_list, 3)
    page = request.GET.get('page') #номер страницы
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/post_list.html', {'posts':posts, 'page':page})

def post_detail(request, year, month, day, slug_post):
    post = get_object_or_404(Post, slug = slug_post,
                                    published_date__year=year,
                                    published_date__month=month,
                                    published_date__day=day)
    comments = post.comments.filter(active = True)
    if request.method == 'POST':
        comment_form = CommentForm(data = request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return redirect("blog:post_detail",year = post.published_date.year,
                                         month = post.published_date.strftime("%m"),
                                         day = post.published_date.strftime("%d"),
                                         slug_post = post.slug)
    else:
        comment_form = CommentForm()
    return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments, 'comment_form': comment_form})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.slug = slugify(post.title)
            post.save()
            return redirect("blog:post_detail",year = post.published_date.year,
                                         month = post.published_date.strftime("%m"),
                                         day = post.published_date.strftime("%d"),
                                         slug_post = post.slug)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form, 'type': 'New post'})

def post_edit(request, year, month, day, slug_post):
    post = get_object_or_404(Post, slug = slug_post,
                                    published_date__year=year,
                                    published_date__month=month,
                                    published_date__day=day)
    if request.method == "POST":
        form = PostForm(request.POST, instance = post)
        if form.is_valid():
            post = form.save()
            return redirect("blog:post_detail",year = post.published_date.year,
                                         month = post.published_date.strftime("%m"),
                                         day = post.published_date.strftime("%d"),
                                         slug_post = post.slug)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form, 'type': 'Editing'})
def post_delete(request, year, month, day, slug_post):
    post = get_object_or_404(Post, slug = slug_post,
                                    published_date__year=year,
                                    published_date__month=month,
                                    published_date__day=day)
    post.delete() 
    return redirect("/")
