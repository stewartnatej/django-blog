"""
ModelAdmin allows us to go beyond the default admin behavior
"""
from django.contrib import admin
from blogging.models import Post, Category


class CategoryInLine(admin.TabularInline):
    """allows us to change categories from the post page"""
    model = Category.posts.through


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [CategoryInLine]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """removes the ability to categorize posts from the category page"""
    exclude = ('posts',)
