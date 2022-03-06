from celery import shared_task


@shared_task
def get_facebook_data(source):
    print(source)
