from django.http import Http404
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import status, authentication, permissions

from .models import MyUser
from .serializers import MyUserSerializer


class MyUserDetail(APIView):
	def get(self, request, username, format=None):
		user = User.objects.get(username=username)
		profile = MyUser.objects.get(user=user)
		serializer = MyUserSerializer(profile)
		return Response(serializer.data)
