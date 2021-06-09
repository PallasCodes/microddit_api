from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Communitie, Category
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
