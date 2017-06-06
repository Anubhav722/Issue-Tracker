# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import pre_save, post_save
from rest_framework.authtoken.models import Token
from django.dispatch import receiver
import random
import string

from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
	user = models.OneToOneField(User)
	access_token = models.CharField(max_length=40)
	# access_token = models.ForeignKey(Token)

	def __unicode__(self):
		return self.user.username

# ACCESS_TOKEN_LENGTH = 40

class Issue(models.Model):
	title = models.CharField(max_length=254)
	description = models.TextField()
	assigned_to = models.ForeignKey(UserProfile, related_name='assigned_to_user')
	created_by = models.ForeignKey(UserProfile, related_name='created_by_user')
	status = models.BooleanField(default=False)

	def __unicode__(self):
		return self.title

# @receiver(post_save, sender=UserProfile)
# def userprofile_pre_save_callback(sender, instance, *args, **kwargs):
#     if not instance.access_token:
#         while(1):
#             # token = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(ACCESS_TOKEN_LENGTH))
#             token = Token.objects.create(user=instance.user)
#             if not UserProfile.objects.filter(access_token=token).exists():
#                 break 
#         instance.access_token = token

@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
	if created:
		token = Token.objects.create(user=instance)

@receiver(post_save, sender=UserProfile)
def create_auth_token_user_profile(sender, instance=None, created=False, **kwargs):
	if created:
		token = Token.objects.last()
		instance.access_token = token.key
		instance.save()