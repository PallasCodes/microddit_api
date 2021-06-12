from django.http import Http404
from django.contrib.auth.models import User

from rest_framework import status, authentication, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .models import Communitie, Category
from myuser.models import MyUser
from .serializers  import CommunitieSerializer, CategorySerializer, CategoriesSerializer, CommunitieDetailSerializer


class CategoryDetails(APIView):
		def get_object(self, category_slug):
				try:
						return Category.objects.get(slug=category_slug)
				except Category.DoesNotExist:
						raise Http404
    
		def get(self, request, category_slug, format=None):
				category = self.get_object(category_slug)
				serializer = CategorySerializer(category)
				return Response(serializer.data)


class CategoriesList(APIView):  
		def get(self, request, format=None):
				categories = Category.objects.all()
				serializer = CategoriesSerializer(categories, many=True)
				return Response(serializer.data)


class CommunitieDetail(APIView):
		def get(self, request, category_slug, communitie_slug, format=None):
				communitie = Communitie.objects.get(slug=communitie_slug)
				serializer = CommunitieDetailSerializer(communitie)
				return Response(serializer.data)


@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def join_communitie(request):
	if not request.data["id"]:
		raise Http404
	else:
		communitie = Communitie.objects.get(pk=request.data["id"])
		serializer = CommunitieDetailSerializer(communitie)
		user = MyUser.objects.get(user=request.user)

		if communitie in user.communities.all():
			user.communities.remove(communitie)
			communitie.num_members -= 1
			communitie.save()
			user.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			user.communities.add(communitie)	
			communitie.num_members += 1
			communitie.save()
			user.save()
			return Response(serializer.data)


class JoinedCommunities(APIView):
	def get(self, request, username, format=None):
		user = User.objects.get(username=username)
		profile = MyUser.objects.get(user=user)
		communities = profile.communities.all()
		serializer = CommunitieDetailSerializer(communities, many=True)
		return Response(serializer.data)