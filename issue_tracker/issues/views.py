# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import viewsets

from issues.models import UserProfile, Issue
from issues.serializers import UserProfileSerializer, IssueSerializer
# Create your views here.
def home(request):
	return HttpResponse("HI there")

class UserProfileViewSet(viewsets.ModelViewSet):
	queryset = UserProfile.objects.all()
	serializer_class = UserProfileSerializer

class IssueViewSet(viewsets.ModelViewSet):
	queryset = Issue.objects.all()
	serializer_class = IssueSerializer