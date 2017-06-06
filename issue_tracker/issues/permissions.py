from rest_framework.permissions import BasePermission
from .models import UserProfile, Issue

class IsOwner(BasePermission):

	def has_object_permission(self, request, view, obj):
		if isinstance(obj, UserProfile):
			return obj.user == request.user

		return obj.user == request.user

class IsCreator(BasePermission):

	def has_object_permission(self, request, view, obj):
		# import ipdb; ipdb.set_trace()
		if isinstance(obj, Issue):
			user = UserProfile.objects.get(user=request.user)
			return obj.created_by == user

		return obj.user == request.user