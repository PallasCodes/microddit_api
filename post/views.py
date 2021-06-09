from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view 
from rest_framework import status, authentication, permissions

from .models import Post
from .serializers import PostSerializer, CreatePostSerializer
from communitie.models import Communitie


class PublicFeed(APIView):
		def get(self, request, format=None):
				posts = Post.objects.all()
				serializer = PostSerializer(posts, many=True)
				return Response(serializer.data)


class Posts(APIView):
		authentication_classes = [authentication.TokenAuthentication]
		permission_classes = [permissions.IsAuthenticated]

		def post(self, request, format=None):
				serializer = CreatePostSerializer(data=request.data)

				if(serializer.is_valid()):
						serializer.save(user=request.user)
						return Response(serializer.data, status=status.HTTP_201_CREATED)
				return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostsFromCommunitie(APIView):
		def get(self, request, communitie_pk, format=None):
				posts = Post.objects.filter(communitie=communitie_pk)
				serializer = PostSerializer(posts, many=True)
				return Response(serializer.data)

