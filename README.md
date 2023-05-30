# A blogging and polling app, using Django
- https://peak-social.herokuapp.com/


# Django
### Managing the app
`python manage.py` ...
- `runserver`
- `migrate`
- `createsuperuser`
- `startapp polling`
- `makemigrations` and then `manage.py migrate`
- `startapp blogging` and then both migration commands
- `test {blogging}` leave out the app name to test all apps


### Shell
Helpful for testing code snippets
- `python manage.py shell`
- `from blogging.models import Post`
- `from django.contrib.auth.models import User`
- `all_users = User.objects.all()`
- `p1 = Post(title='My First Post', text='My first text')`
- `p1.author = all_users[0]`
- `p1.save()`


# Travis CI
If the database is not in the repo, you can create it with `python manage.py migrate` in .travis.yml.
For this to work, you'll need to run `makemigrations` and commit the migration files to the repo.
Environment variables are handled in the Travis UI.


# Heroku
### Initial setup
- `heroku create peak-social`
- `heroku config:set DJANGO_SETTINGS_MODULE=frog_jog_blog.heroku` uses heroku-specific settings
- `heroku config:set django_key={secret key}`
- `heroku addons:create heroku-postgresql:mini`
- `heroku config` shows the environment variables
- `heroku run python manage.py createsuperuser` creates django superuser

### Manually deploying updates
- ensure requirements.txt is updated
- ensure changes are committed to your desired branch
  - `git push heroku main` if changes are committed to `main`
  - `git push heroku dev:main` if changes are committed to `dev`
- `heroku open`

### Continuous Deployment
Configured in Heroku UI


# black
`black {--check} blogging frog_jog_blog polling`
- running without `--check` will reformat the file


# requirements.txt
It's better to be specific about package versions.
I want to run 3.11 on Heroku, but Travis doesn't offer 3.11.
Keeping the versions ambiguous ensures they can be installed on both systems.
The important thing is the Django version, due to some breaking changes.


# async
I never found a way to implement async templates, so the below info is just for historical purposes.
More info about that adventure can be found in polling\views.py

### Launch the app asynchronously:
`python -m uvicorn frog_jog_blog.asgi:application`. When running in dev environment, add `--reload`

This just spawns a single process, which is usually sufficient for dev. For a production app you may want more.
You can use uvicorn to spawn multiple workers by adding `--workers 4`,
but this is not as robust as using gunicorn with uvicorn worker classes:
- https://fastapi.tiangolo.com/deployment/server-workers/
- https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/uvicorn/#deploying-django-using-uvicorn-and-gunicorn
