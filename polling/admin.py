from django.contrib import admin
from polling.models import Poll

# allow us to manage the database on the admin page
admin.site.register(Poll)
