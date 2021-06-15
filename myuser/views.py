from django.http import Http404
from django.contrib.auth.models import User
from django.db.models import Q

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


@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def create_profile(request):
		profile = MyUser(user=request.user,name=request.data['username'])
		profile.save()
		serializer = MyUserSerializer(profile)
		return Response(serializer.data, status.HTTP_201_CREATED)


@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def follow_or_unfollow(request):
		followed_user = User.objects.get(username=request.data['username'])
		user = MyUser.objects.get(user=request.user)
		if followed_user in user.friends.all():
			user.friends.remove(followed_user)
			return Response("user deleted")
		else:
			serializer = MyUserSerializer(followed_user)
			user.friends.add(followed_user)
			return Response(serializer.data, status.HTTP_201_CREATED)


@api_view(['GET'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def get_followed(request):
		user = MyUser.objects.get(user=request.user)
		followed = []
		for friend in user.friends.all():
			followed.append(User.objects.get(pk=friend.id))
		serializer = MyUserSerializer(followed, many=True)
		return Response(serializer.data)


@api_view(['PUT'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def update_profile(request):
		serializer = MyUserSerializer(data=request.data)

		if serializer.is_valid():
			profile = MyUser.objects.get(user=request.user)
			profile.bio_description = request.data["bio_description"]
			profile.name = request.data["name"]
			profile.save()
			return Response(serializer.data)


class SearchUser(APIView):
		def get(self, request, query, format=None):
	  		users = MyUser.objects.filter(Q(name__icontains=query))
	  		serializer = MyUserSerializer(users, many=True)
	  		return Response(serializer.data)

