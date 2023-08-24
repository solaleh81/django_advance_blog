from typing import Any, Optional
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from .models import Post
from .forms import PostForm


# Create your views here.


def indexView(request):
    """
    a function base view to show index page
    """
    name = "ali"
    context = {"name": name}
    return render(request, "index.html")


class IndexView(TemplateView):
    """
    a class based view to show index page
    """

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "ali"
        context["posts"] = Post.objects.all()
        return context


"""
a fbv def for redirect
"""


def redirectToMaktab(request):
    return redirectToMaktab("https://maktabkhoneh.com")


"""
a cbv for redirect
"""


class RedirectToMaktab(RedirectView):
    url = "https://maktabkhooneh.com"

    def get_redirect_url(self, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs["pk"])
        print(post)
        return super().get_redirect_url(*args, **kwargs)


class PostList(ListView):
    model = Post
    queryset = Post.objects.all()
    context_object_name = "posts"
    paginate_by = 2
    ordering = "id"

    def get_queryset(self):
        posts = Post.objects.filter(status=False)
        return posts


class PostDetailView(DetailView):
    model = Post


# class PostCreateView(FormView):
#     template_name = "contact.html"
#     form_class = PostForm
#     contact_url = "/blog/post/"

#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)


class PostCreateView(CreateView):
    model = Post
    # fields = ["author", "title", "content", "status", "published_date"]
    form_class = PostForm
    success_url = "/blog/post/"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostEditView(UpdateView):
    model = Post
    form_class = PostForm
    success_url = "/blog/post/"


class PostDeleteView(DeleteView):
    model = Post
    success_url = "/blog/post/"
    template_name = "post_confirm_delete.html"
