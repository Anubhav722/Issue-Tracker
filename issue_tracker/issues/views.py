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
# Create your views here.
def home(request):
	return HttpResponse("HI there")

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
			# serializer.save(created_by=self.request.user)
		except Exception as e:
			raise (e)

# def send_email(data):
	
