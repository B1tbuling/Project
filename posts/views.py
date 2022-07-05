from django.views.generic import View

from .utils import *
from .forms import TagForm, PostForm


class PostsList(ObjectsListMixin, View):
    model = Post
    template = 'blog/index.html'


class TagsList(ObjectsListMixin, View):
    model = Tag
    template = 'blog/tags_list.html'


class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'


class PostCreate(ObjectCreateMixin, View):
    model_form = PostForm
    template = 'blog/post_create_form.html'


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'


class TagCreate(ObjectCreateMixin, View):
    model_form = TagForm
    template = 'blog/tag_create.html'
