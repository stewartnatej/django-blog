from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from polling.models import Poll
from asgiref.sync import sync_to_async


def list_view(request):
    """function version of the view"""
    context = {'polls': Poll.objects.all()}
    return render(request, 'polling/list.html', context)


class PollListView(ListView):
    """more robust class-based view"""
    model = Poll
    template_name = 'polling/list.html'


async def list_view_async(request):
    """
    experiment in async. could not find a way to make the template render asynchronously.
    the only thing i got working was adding the below in settings.py, but that's not good.
    os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
    https://docs.djangoproject.com/en/4.2/topics/async/#envvar-DJANGO_ALLOW_ASYNC_UNSAFE
    """
    polls = await sync_to_async(Poll.objects.all)()  # ORM is not async (yet)
    context = {'polls': polls}
    return render(request, 'polling/list.html', context)


def detail_view(request, poll_id):
    """function version of the view"""
    try:
        poll = Poll.objects.get(pk=poll_id)
    except Poll.DoesNotExist:
        raise Http404

    if request.method == 'POST':
        if request.POST.get('vote') == 'Yes':
            poll.score += 1
        else:
            poll.score -= 1
        poll.save()

    context = {'poll': poll}
    return render(request, 'polling/detail.html', context)


class PollDetailView(DetailView):
    """more robust class-based view"""
    model = Poll
    template_name = 'polling/detail.html'

    def post(self, request, *args, **kwargs):
        poll = self.get_object()

        if request.POST.get("vote") == "Yes":
            poll.score += 1
        else:
            poll.score -= 1
        poll.save()

        context = {"poll": poll}
        return render(request, self.template_name, context)
