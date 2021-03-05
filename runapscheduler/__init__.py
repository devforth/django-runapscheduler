# -*- coding: utf-8 -*-
__version__ = '1.0.1'

default_app_config = 'runapscheduler.apps.ApschedulerAppConfig'


def scheduled_job(*args, **kwargs):
    from runapscheduler.proxy import job_proxy
    return job_proxy.scheduled_job(*args, **kwargs)
