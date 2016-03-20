worker: redis-server
celery1: celery -A gleam.celery worker -l info
celery2: celery -A gleam beat -S djcelery.schedulers.DatabaseScheduler -l info