from django_celery_beat.models import PeriodicTask, IntervalSchedule


schedule, created = IntervalSchedule.objects.get_or_create(
    every=900,
    period=IntervalSchedule.SECONDS,
)
PeriodicTask.objects.create(
    interval=schedule,
    name='Updating DB',
    task='updtrends.tasks.task_update_db',
)