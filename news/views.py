from django.shortcuts import render, redirect
from updtrends.models import ActualNews
from django.views.generic import View
from .forms import SheduleForm
from django.contrib import messages

from updtrends.tasks import task_update_db
from django_celery_beat.models import IntervalSchedule


class NewsList(View):
    def get(self, request):
        try:
            if IntervalSchedule.objects.all()[0]:
                form = SheduleForm(initial={'timeout': IntervalSchedule.objects.all()[0].every})
        except Exception:
            pass
        posts = ActualNews.objects.all()
        return render(request, 'index.html', context={'posts': posts, 'form': form})

    def post(self, request):
        posts = ActualNews.objects.all()
        form = SheduleForm(request.POST)
        if form.is_valid():
            timeout = form.cleaned_data['timeout']
            schedule = IntervalSchedule.objects.all()[0]
            schedule.every = timeout
            schedule.save()
            messages.add_message(request, messages.INFO, 'Updating every {} seconds'.format(timeout))
        return render(request, 'index.html', context={'posts': posts, 'form': form})


def update_db(request):
    messages.add_message(request, messages.INFO, 'Updating database. Reload the page in a few seconds')
    task_update_db.delay()
    return redirect('/')