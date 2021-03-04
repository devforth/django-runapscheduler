# Django Run APScheduler Command
Django Run APScheduler Command is a command that simplifies management of scheduler for django apps and moves those tasks to a separate django process, so you can run heavy tas without worrying of django app stalling.

To use the command firstly you need to create scheduler.py file inside your app and attach `runapscheduler.scheduled_job` decorator to any function.

`runapscheduler.scheduled_job` decorator accepts the same parameters as `APSceduler`'s [scheduled_job](https://apscheduler.readthedocs.io/en/stable/modules/schedulers/base.html#apscheduler.schedulers.base.BaseScheduler.scheduled_job) decorator.


Also it's possible to pass some options to schedulers. To do add `RUNAPSCHEDULER_OPTIONS` dictionary to `setting.py`.
First key must be a name of scheduler and the value of that key must be a dict filled as in [Method 2](https://apscheduler.readthedocs.io/en/stable/userguide.html#configuring-the-scheduler) in APScheduler documentation.
Example:
```
RUNAPSCHEDULER_OPTIONS = {
    'BackgroundScheduler': {
        'apscheduler.jobstores.default': {
            'type': 'sqlalchemy',
            'url': 'sqlite:///jobs.sqlite'
        },
        'apscheduler.executors.default': {
            'class': 'apscheduler.executors.pool:ThreadPoolExecutor',
            'max_workers': '20'
        },
        'apscheduler.job_defaults.coalesce': 'false',
        'apscheduler.job_defaults.max_instances': '3',
        'apscheduler.timezone': 'UTC',
    }
}
```