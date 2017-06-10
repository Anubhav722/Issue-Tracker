# launchyard_task

### Install all the dependencies
```
$ pip install -r requirements.txt
```
### Make sure redis server is running
```
$ redis-cli ping
PONG
```
It should reply with PONG.

### Endpoints associated
1) /issues/
2) /users/

### In the virtualenv, cd into issue_tracker:
Keep the server running ie. (./manage.py runserver)
In one terminal window: Fire up Celery worker
```
$ celery -A issue_tracker worker -l info
```
In other terminal window: Fire up Celery task scheduler
```
$ celery -A issue_tracker beat -l info
```
## NOTE: Have used mailgun which requires verification of emails for free services. To see the emails in action, add the following line in settings.py file:
```
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```
### Fetching access_token for a user:
![alt text](https://raw.githubusercontent.com/Anubhav722/launchyard_task/master/postman_images/postman_post.png)

### Fetching links via access_token:
![alt_text](https://raw.githubusercontent.com/Anubhav722/launchyard_task/master/postman_images/postman_get.png)
