from celery.decorators import task
from celery.utils.log import get_task_logger

from celery.task.schedules import crontab
from celery.decorators import periodic_task

from issues.utils import send_mails_daily, send_mails

logger = get_task_logger(__name__)


@periodic_task(
	run_every=(crontab(minute='*/2')),
	name = 'send_mails_after_24_hours',
	ignore_result = True
)
def send_emails_after_24_hours():
	"""
	Sends emails for issues after every 24 hours
	"""
	send_mails_daily()
	logger.info("Send mails daily")


@task(name='send_email_after_12_minutes_for_issue_creation_task')
def send_mail_after_12_minutes_for_issue_creation_task(email, subject, message):
	"""
	Sends email to users who have been assigned an issue 
	exactly after 12 minutes successfully.
	"""
	logger.info('Send issue creation email')
	send_mails(email, subject, message)
