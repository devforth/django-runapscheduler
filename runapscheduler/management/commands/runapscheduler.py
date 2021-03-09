from runapscheduler.proxy import job_proxy
from django.core.management.base import BaseCommand
from django.utils.module_loading import autodiscover_modules
from apscheduler.schedulers.blocking import BlockingScheduler

class Command(BaseCommand):
  help = 'Starts schedulers for registered apps'
  requires_system_checks = True

  def handle(self, *args, **options):
    self.stdout.write(f"⚪ Starting scheduler")

    autodiscover_modules('scheduler')
    jobs = job_proxy.get_jobs()

    if len(jobs) == 0:
      self.stdout.write("❌ No scheduler jobs were found. Exiting...")
    else:
      self.stdout.write(f"📦 Found {len(jobs)} job(s) in [{', '.join(map(lambda job: job.func.__wrapped__.__module__.split('.')[0], jobs))}] app(s).")

      job_proxy.start_schedulers()

      # start empty blocking scheduler so command doesn't exit
      heartbeat_scheduler = BlockingScheduler()

      self.stdout.write(f"✅ Scheduler started")

      heartbeat_scheduler.start()
