web: daphne gleam.asgi:channel_layer --port $PORT --bind 0.0.0.0 -v2
worker: python manage.py runworker -v2
celery1: celery -A gleam.celery worker -l info
celery2: celery -A gleam beat -S djcelery.schedulers.DatabaseScheduler -l info