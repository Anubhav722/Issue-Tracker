from rest_framework import serializers
from issues.models import UserProfile, Issue

class UserProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserProfile
		fields = ['id', 'user', 'access_token']

class IssueSerializer(serializers.ModelSerializer):
	class Meta:
		model = Issue
		fields = ['title', 'description', 'assigned_to', 'created_by', 'status']