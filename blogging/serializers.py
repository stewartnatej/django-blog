from django.contrib.auth.models import User
from rest_framework.serializers import HyperlinkedModelSerializer, SerializerMethodField
from blogging.models import Post, Category


class UserSerializer(HyperlinkedModelSerializer):
    """show all details about an author"""

    class Meta:
        model = User
        fields = ["username", "last_login", "is_active", "is_staff", "is_superuser"]


class AuthorSerializer(HyperlinkedModelSerializer):
    """only show the username, for use in the Post API"""

    class Meta:
        model = User
        fields = ["username"]


class PostSerializer(HyperlinkedModelSerializer):
    author = AuthorSerializer()  # nested object with ForeignKey field

    class Meta:
        model = Post
        fields = ["title", "text", "published_date", "author"]


class CategorySerializer(HyperlinkedModelSerializer):
    posts = PostSerializer(many=True)  # nested object with ManyToManyField

    class Meta:
        model = Category
        fields = ["name", "description", "posts"]
