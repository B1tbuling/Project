from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.views.generic import View

from .models import Post, Tag
from .utils import *
from .forms import TagForm, PostForm

from django.http import HttpResponse, Http404

class PostsList(ObjectsListMixin, View):

    model = Post
    template = 'blog/index.html'

    # def get(self, request):
    #     posts = Post.objects.all()
    #     return render(request, 'blog/index.html', context={'posts': posts})


class TagsList(ObjectsListMixin, View):

    model = Tag
    template = 'blog/tags_list.html'

    # def get(self, request):
    #     tags = Tag.objects.all()
    #     return render(request, 'blog/tags_list.html', context={'tags': tags })


class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'
    # def get(self, request, slug):
    #     post = get_object_or_404(Post, slug__iexact=slug)
    #     return render(request, 'blog/post_detail.html', context={'post': post})


class PostCreate(ObjectCreateMixin, View):
    model_form = PostForm
    template = 'blog/post_create_form.html'


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'
    # def get(self, request, slug):
    #     tag = get_object_or_404(Tag, slug__iexact=slug)
    #     return render(request, 'blog/tag_detail.html', context={'tag': tag})

        # Аналог записи
        # tags = Tag.objects.filter(slug__iexact=slug)
        # if len(tags) > 0:
        #     tag = tags[0]
        #     return render(request, 'blog/tag_detail.html', context={'tag': tag})
        # else:
        #     raise Http404()


class TagCreate(ObjectCreateMixin, View):
    model_form = TagForm
    template = 'blog/tag_create.html'

# def tag_detail(request, slug):
#     tag = Tag.objects.get(slug__iexact=slug)
#     return render(request, 'blog/tag_detail.html', context={'tag': tag})

# def post_detail(request, slug):
#     post = Post.objects.get(slug__iexact=slug)
#     return render(request,'blog/post_detail.html', context={'post': post})


