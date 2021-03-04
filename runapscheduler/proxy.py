from typing import Dict
from django.conf import settings
from django.utils import timezone
from apscheduler.schedulers.base import BaseScheduler
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler


def log_start_end_decorator(function):
    def wrapper(*args, **kwargs):
        func_name = f'{function.__module__}.{function.__name__}'

        print(f"\n{timezone.now().ctime()}: '{func_name}' started execution.")
        result = function(*args, **kwargs)
        print(f"{timezone.now().ctime()}: '{func_name}' finished execution.\n")
        return result
    return wrapper


class JobProxy():
    def __init__(self):
        self.schedulers: Dict[type, BaseScheduler] = {}

    def _get_scheduler(self, scheduler_class):
        if not issubclass(scheduler_class, BaseScheduler):
            raise TypeError("'scheduler_class' must be a subclass of 'apscheduler.schedulers.base.BaseScheduler'")

        if type(scheduler_class) == BlockingScheduler:
            raise TypeError("'scheduler_class' can not be 'apscheduler.schedulers.base.BlockingScheduler' type")

        if scheduler_class not in self.schedulers:
            schedulers_options = getattr(settings, 'RUNAPSCHEDULER_OPTIONS', {})
            scheduler_options = schedulers_options.get(scheduler_class.__name__, {})

            self.schedulers[scheduler_class] = scheduler_class(scheduler_options)
        return self.schedulers[scheduler_class]

    def get_jobs(self):
        jobs = []

        for scheduler in self.schedulers.values():
            jobs.extend(scheduler.get_jobs())

        return jobs

    def start_schedulers(self):
        for scheduler in self.schedulers.values():
            scheduler.start()

    def scheduled_job(self, *args, scheduler_class=BackgroundScheduler, **kwargs):
        scheduler: BaseScheduler = self._get_scheduler(scheduler_class)
        inner = scheduler.scheduled_job(*args, **kwargs)
        return lambda f: inner(log_start_end_decorator(f))

job_proxy = JobProxy()