from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import status, authentication, permissions

from .models import Post, Reaction
from .serializers import PostSerializer, CreatePostSerializer, ReactionSerializer, AuthPostSerializer
from communitie.models import Communitie


class PublicFeed(APIView):
		def get(self, request, format=None):
				posts = Post.objects.all()
				if request.user.is_authenticated:
					serializer = AuthPostSerializer(posts, many=True)
					print(request.user)
				else:
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


@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def react_to_post(request):
	serializer = ReactionSerializer(data=request.data)

	if serializer.is_valid():
		try:
			reaction = Reaction.objects.get(user=request.user, post=request.data['post'])
			if reaction.reaction == request.data['reaction']:
				reaction.reaction = None
			else:
				reaction.reaction = not reaction.reaction
			reaction.save()
			serializer_response = ReactionSerializer(reaction)
			return Response(serializer_response.data, status.HTTP_201_CREATED)

		except Exception:	
			serializer.save(user=request.user)
		
		return Response(serializer.data, status.HTTP_201_CREATED)

	return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)