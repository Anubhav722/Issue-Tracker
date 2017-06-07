# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from issues.models import UserProfile, Issue
from issues.serializers import UserProfileSerializer, IssueSerializer
from .permissions import IsOwner, IsCreator
from issues.tasks import send_mail_after_12_minutes_for_issue_creation_task
# Create your views here.
def home(request):
	return HttpResponse("HI there")

def send_issue_creation_email(self):
	queryset = self.queryset.last()
	email = queryset.assigned_to.user.email
	assigned_user = queryset.assigned_to.user.username
	created_user = queryset.created_by.user.username
	issue_title = queryset.title
	issue_description = queryset.description
	issue_status = queryset.status
		
	subject = ('The issue {}'.format(issue_title))

	message = ('Hi {},\n {} has assigned you an issue \n Issue: {} \n \
		Description: {} \n Status: {}\
		'.format(assigned_user, created_user, issue_title, issue_description, issue_status))

	send_mail_after_12_minutes_for_issue_creation_task.apply_async((email, subject, message), countdown=720)


class UserProfileViewSet(viewsets.ModelViewSet):
	queryset = UserProfile.objects.all()
	serializer_class = UserProfileSerializer
	permission_classes = (IsAuthenticated, IsOwner)

class IssueViewSet(viewsets.ModelViewSet):
	queryset = Issue.objects.all()
	serializer_class = IssueSerializer
	permission_classes = (IsAuthenticated, IsCreator)

	# specify perform_create for assigned user here
	def perform_create(self, serializer):
		try:
			user = UserProfile.objects.get(user=self.request.user)
			serializer.save(created_by=user)
			send_issue_creation_email(self)

		except Exception as e:
			raise (e)
