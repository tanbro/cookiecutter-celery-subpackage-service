from celery import Celery

__all__ = ['app']

app = Celery('.'.join(__name__.split('.')[:-1]))
