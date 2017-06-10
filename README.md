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

### activate the virtualenv and cd into issue_tracker:
Keep the server running ie. (./manage.py runserver)
In one terminal window: Fire up Celery worker
```
$ celery -A issue_tracker worker -l info
```
In other terminal window: Fire up Celery task scheduler
```
$ celery -A issue_tracker beat -l info
```
### Fetching access_token for a user:
![alt text](https://raw.githubusercontent.com/Anubhav722/launchyard_task/master/postman_images/postman_post.png)

### Fetching links via access_token:
![alt_text](https://raw.githubusercontent.com/Anubhav722/launchyard_task/master/postman_images/postman_get.png)
