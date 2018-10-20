from .sync import upd_dbnews, upd_dbtrends
from celery import task
from updtrends.actualproc import create_actual_posts


@task(name='task_update_db')
def task_update_db():
    upd_dbnews()
    upd_dbtrends()
    create_actual_posts()
    return 'DB updated'
