from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions, filters
from blogging.models import Post, Category
from blogging.serializers import PostSerializer, CategorySerializer, UserSerializer


# ---------- UI Display ----------- #
# these views are used by the website
def stub_view(request, *args, **kwargs):
    """generic view to use while templates/models are being built"""
    body = "Stub View\n\n"
    if args:
        body += "Args:\n"
        body += "\n".join(["\t%s" % a for a in args])
    if kwargs:
        body += "Kwargs:\n"
        body += "\n".join(["\t%s: %s" % i for i in kwargs.items()])
    return HttpResponse(body, content_type="text/plain")


def list_view(request):
    """function version of the view"""
    published = Post.objects.exclude(published_date__exact=None)
    posts = published.order_by("-published_date")
    context = {"posts": posts}
    return render(request, "blogging/list.html", context)


class PostListView(ListView):
    """more robust class-based view"""

    queryset = Post.objects.exclude(published_date__exact=None).order_by(
        "-published_date"
    )
    template_name = "blogging/list.html"


def detail_view(request, post_id):
    """function version of the view"""
    published = Post.objects.exclude(published_date__exact=None)
    try:
        post = published.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404
    context = {"post": post}
    return render(request, "blogging/detail.html", context)


class PostDetailView(DetailView):
    """more robust class-based view"""

    queryset = Post.objects.exclude(published_date__exact=None)
    template_name = "blogging/detail.html"


# ------- API Access ---------- #
# these views are used by the API
# order_by enables pagination
# lookup_field makes urls more readable. it's case-sensitive. for spaces, /my%20first%20post
# permissions.IsAuthenticatedOrReadOnly lets you browse data even if not logged in
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by("-published_date")
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = "title"

    filter_backends = [filters.SearchFilter]
    search_fields = [
        "author__username"
    ]  # filter based on the author. /api/posts?search=anonymous


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("username")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = "username"


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by("name")
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = "name"

    filter_backends = [filters.SearchFilter]
    search_fields = ["name"]  # /api/categories?search=qa
