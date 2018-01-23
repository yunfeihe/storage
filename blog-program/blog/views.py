from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post, Category, Tag, SinglePage
import markdown
from comments.forms import CommentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


def index(request):
    page_index = int(request.GET.get('page') or 1)
    post_pages = Paginator(Post.objects.all(), 8)
    post_pages.page_number_list = post_pages.page_range
    post_pages.page_index = page_index
    if page_index in post_pages.page_range:
        return render(request, 'blog/index.html', {
            'post_list': post_pages.page(page_index),
            'post_pages': post_pages,

        })


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.auto_increase_views() #统计阅读量
    post.body = markdown.markdown(post.body, extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
    ])
    form = CommentForm()
    comment_list = post.comment_set.all()
    context = {
        'post': post,
        'form': form,
        'comment_list': comment_list,
    }
    return render(request, 'blog/detail.html', context)


def archives(request, year, month):
    page_index = int( request.GET.get('page') or 1 )
    post_list = Post.objects.filter(
        created_time__year=year,
        created_time__month=month,
    )
    post_pages = Paginator(post_list, 8)
    post_pages.page_number_list = post_pages.page_range
    post_pages.page_index = page_index
    if page_index in post_pages.page_range:
        return render(request, 'blog/index.html', {

            'post_list': post_pages.page(page_index),
            'post_pages': post_pages,
            })


def category(request, pk):
    page_index = int(request.GET.get('page') or 1)
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.all().filter(category=cate).order_by('-created_time')
    post_pages = Paginator(post_list, 8)
    post_pages.page_number_list = post_pages.page_range
    post_pages.page_index = page_index
    if page_index in post_pages.page_range:
        return render(request, 'blog/index.html', {

            'post_list': post_pages.page(page_index),
            'post_pages':post_pages,

            })

def tag(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    page_index = int(request.GET.get('page') or 1)
    post_pages = Paginator(tag.get_posts_of_self(), 8)
    
    post_pages.page_index = page_index
    if page_index in post_pages.page_range:
        return render(request, 'blog/index.html',{
            'post_list': post_pages.page(page_index),
            'post_pages': post_pages,
            })

def single(request, name):
    single_page = get_object_or_404(SinglePage, name=name)
    return render(request, 'blog/single.html', {'post':single_page})
