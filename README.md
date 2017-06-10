# launchyard_task

### activate the virtualenv and cd into issue_tracker:
Keep the server running ie. (./manage.py runserver)
in one terminal window worker
```
$ celery -A issue_tracker worker -l info
```
in other terminal window
```
$ celery -A issue_tracker beat -l info
```
### Fetching access_token for a user:
