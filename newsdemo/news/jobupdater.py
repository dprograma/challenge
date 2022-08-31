from apscheduler.schedulers.background import BackgroundScheduler
from .cron import job

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(job, 'interval', minutes=2)
    scheduler.start()
