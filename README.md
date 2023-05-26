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
I never found a way to implement async templates, so the below info is just for historical purposes.
More info about that adventure can be found in polling\views.py

### Launch the app:
`python -m uvicorn frog_jog_blog.asgi:application`. When running in dev environment, add `--reload`

This just spawns a single process, which is usually sufficient for dev. For a production app you may want more.
You can use uvicorn to spawn multiple workers by adding `--workers 4`,
but this is not as robust as using gunicorn with uvicorn worker classes:
- https://fastapi.tiangolo.com/deployment/server-workers/
- https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/uvicorn/#deploying-django-using-uvicorn-and-gunicorn
