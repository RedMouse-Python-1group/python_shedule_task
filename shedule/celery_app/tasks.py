# -*- coding: utf-8 -*-

from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger
# from datetime import datetime
import datetime

from celery_app.models import CeleryApp

logger = get_task_logger(__name__)

# A periodic task that will run every minute (the symbol "*" means every)
# @periodic_task(run_every=(crontab(minute="*/1")))
@periodic_task(run_every=datetime.timedelta(minutes=1))
def scraper_example():
    logger.info("Start task")
    now = datetime.datetime.now()
    s = CeleryApp(field1=str(now), field2=str(now))
    s.save()
    logger.info("Task finished: result = %s" % str(now))