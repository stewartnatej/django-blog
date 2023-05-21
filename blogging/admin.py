from django.contrib import admin
from blogging.models import Post, Category

# allow us to manage the database on the admin page
admin.site.register(Post)
admin.site.register(Category)
