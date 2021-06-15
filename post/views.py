from django.http import Http404
from django.contrib.auth.models import User
from django.db.models import Q
from django.core.paginator import Paginator

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import status, authentication, permissions
from rest_framework.pagination import PageNumberPagination

from .models import Post, Reaction, Comment
from .serializers import PostSerializer, CreatePostSerializer, ReactionSerializer, AuthPostSerializer, FullPostSerializer, CommentSerializer
from communitie.models import Communitie
from myuser.models import MyUser


class PublicFeed(APIView):
		def get(self, request, format=None):
				paginator = PageNumberPagination()
				if request.user.is_authenticated:
					user = MyUser.objects.get(user=request.user)
					friends = user.friends.all()
					communities = user.communities.all()
					posts = Post.objects.filter(Q(user_id__in=friends) | Q(communitie_id__in=communities) | Q(user_id=request.user))
					page = paginator.paginate_queryset(posts, request)
					serializer = AuthPostSerializer(page, many=True)
				else:
					communities = Communitie.objects.all()
					posts = Post.objects.filter(Q(communitie_id__in=communities))
					page = paginator.paginate_queryset(posts, request)
					serializer = PostSerializer(page, many=True)
				return Response(serializer.data)


class AllPosts(APIView):
	def get(self, request, format=None):
		paginator = PageNumberPagination()
		posts = Post.objects.all()
		page = paginator.paginate_queryset(posts, request)
		serializer = PostSerializer(page, many=True)
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


class FullPost(APIView):
	def get(self, request, post_id ,format=None):
			post = Post.objects.get(pk=post_id)
			serializer = FullPostSerializer(post)
			return Response(serializer.data)


class Comments(APIView):
	def get(self, request, post_id ,format=None):
			comments = Comment.objects.filter(post=post_id)
			serializer = CommentSerializer(comments, many=True)
			return Response(serializer.data)


@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def comment_post(request):
	serializer = CommentSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save(user=request.user)
		return Response(serializer.data, status.HTTP_201_CREATED)

	return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class PostsFromProfile(APIView):
		def get(self, request, username, format=None):
				user = User.objects.get(username=username)
				posts = Post.objects.filter(user=user)
				serializer = PostSerializer(posts, many=True)
				return Response(serializer.data)


class SearchPost(APIView):
		def get(self, request, query, format=None):
	  		posts = Post.objects.filter(Q(title__icontains=query))
	  		serializer = PostSerializer(posts, many=True)
	  		return Response(serializer.data)


@api_view(['DELETE'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def delete_post(request, post_id):
		post = Post.objects.get(pk=post_id)

		if post.user != request.user:
			return Response("This user can't delete this post", status.HTTP_403_FORBIDDEN)

		post.delete()
		return Response('Post deleted')
