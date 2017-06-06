from django.contrib.auth.models import User

from rest_framework import serializers
from issues.models import UserProfile, Issue

# class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
# class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
# 	access_token = serializers.CharField(max_length=30, source = 'userprofile.access_token')
# 	class Meta:
# 		model = User
# 		fields = ['id', 'email', 'username', 'first_name', 'last_name', 'password', 'access_token']
# 		# fields = '__all__

# 		def create(self, validated_data):
# 			import ipdb; ipdb.set_trace()
# 			return UserProfile.objects.create(**validated_data)

# 		def update(self, instance, validated_data):
# 			instance.email = validated_data.get('email', instance.email)
# 			instance.username = validated_data.get('username', instance.username)
# 			instance.first_name = validated_data.get('first_name', instance.first_name)
# 			instance.last_name = validated_data.get('last_name', instance.last_name)
# 			instance.password = validated_data.get('password', instance.password)
# 			instance.access_token = validated_data.get('access_token', instance.access_token)
# 			instance.save()
# 			return instance

# wherever neccessary provide 'ReadOnlyField'
class UserProfileSerializer(serializers.ModelSerializer):
	username = serializers.CharField(source = 'user.username')
	email = serializers.CharField(source = 'user.email')
	first_name = serializers.CharField(source = 'user.first_name')
	last_name = serializers.CharField(source = 'user.last_name')
	password = serializers.CharField(source = 'user.password')
	# access_token = serializers.CharField(max_length=30)

	class Meta:
		model = User
		fields = ['id', 'email', 'username', 'first_name', 'last_name', 'password']

	def create(self, validated_data):
		user = User.objects.create_user(
			email = validated_data['user']['email'],
			username = validated_data['user']['username'],
			first_name = validated_data['user']['first_name'],
			last_name = validated_data['user']['last_name'],
			password = validated_data['user']['password'],
			)
		return UserProfile.objects.create(user=user)

	def update(self, instance, validated_data):
		# import ipdb; ipdb.set_trace()
		instance.user.email = validated_data.get('user')['email']
		instance.user.username = validated_data.get('user')['username']
		instance.user.first_name = validated_data.get('user')['first_name']
		instance.user.last_name = validated_data.get('user')['last_name']
		instance.user.password = validated_data.get('user')['password']
		instance.user.save()
		instance.access_token = validated_data.get('access_token', instance.access_token)
		instance.save()
		return instance

class IssueSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Issue
		fields = ['title', 'description', 'assigned_to', 'created_by', 'status']
		read_only_fields = ('created_by',)