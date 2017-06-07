from issues.models import Issue
import requests

def get_all_issues():
	"""
	Grabs all the issues created
	"""
	emails = []
	usernames = []
	titles = []
	descriptions = []
	statuss = []

	issues = Issue.objects.all()
	for issue in issues:
		emails.append(issue.assigned_to.user.email)
		usernames.append(issue.assigned_to.user.username)
		titles.append(issue.title)
		descriptions.append(issue.description)
		statuss.append(issue.status)

	return (emails, usernames, titles, descriptions, statuss)

def send_mails_daily():
	emails, usernames, titles, descriptions, statuss = get_all_issues()
	try:
		url = 'https://api.mailgun.net/v3/sandbox886b3194f17e4e6fa6e0169d2e4da267.mailgun.org/messages'

		for index in xrange(len(titles)):
			title = titles[index]
			description = descriptions[index]
			email = emails[index]
			username = usernames[index]
			stat = statuss[index]


			subject = ('{}'.format(title))
			text = ('Hi {}, "\n"Title: {} "\n", Description: {} "\n", Status: {}'.format(username, title, description, stat))

			send_mails(email, subject, text)

	except Exception as e:
		raise e


def send_mails(email, subject, message):
	try:
		url = 'https://api.mailgun.net/v3/sandbox886b3194f17e4e6fa6e0169d2e4da267.mailgun.org/messages'

		status = requests.post(
				url,
				auth = ('api', 'key-ca3b1c42c10e96d7a83d43409b2047bb'),
				data = {'from': 'mailgun@sandbox886b3194f17e4e6fa6e0169d2e4da267.mailgun.org',
						 'to': email,
						 'subject': subject,
						 'text': message,
						 'html': '',

					}
			)
		return status

	except Exception as e:
		raise e