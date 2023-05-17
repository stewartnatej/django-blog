# A blog, on Django
- http://127.0.0.1:8000
- Admin console: http://127.0.0.1:8000/admin

# Commands
After `python manage.py`
- `runserver`
- `migrate`
- `createsuperuser`
- `startapp polling`
- `makemigrations` and then `manage.py migrate`
- `startapp blogging` and then both migration commands
- `test blogging`

# Django shell
Helpful for testing code snippets
- `python manage.py shell`
- `from blogging.models import Post`
- `from django.contrib.auth.models import User`
- `all_users = User.objects.all()`
- `p1 = Post(title='My First Post', text='My first text')`
- `p1.author = all_users[0]`
- `p1.save()`

# async
`python -m uvicorn frog_jog_blog.asgi:application`

If the pain outweighs how much we wind up using async, potentially uninstall uvicorn before deploying to Heroku.

Should we use gunicorn with uvicorn workers?
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/uvicorn/#deploying-django-using-uvicorn-and-gunicorn
