from django.contrib.auth.models import User
from rest_framework.serializers import HyperlinkedModelSerializer
from blogging.models import Post, Category


class PostSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = [
            "title",
            "text",
            "published_date",
        ]  # adding author makes it fail


class UserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["username", "last_login", "is_active", "is_staff", "is_superuser"]


class CategorySerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ["name", "description"]  # adding posts makes it fail
