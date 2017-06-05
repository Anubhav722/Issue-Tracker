# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
	user = models.OneToOneField(User)
	access_token = models.CharField(max_length=30)

	def __unicode__(self):
		return self.user.username

class Issue(models.Model):
	title = models.CharField(max_length=254)
	description = models.TextField()
	assigned_to = models.ForeignKey(UserProfile, related_name='assigned_to_user')
	created_by = models.ForeignKey(UserProfile, related_name='created_by_user')
	status = models.BooleanField(default=False)

	def __unicode__(self):
		return self.title