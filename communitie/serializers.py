from rest_framework import serializers

from .models import Communitie, Category


class CommunitieSerializer(serializers.ModelSerializer):
		class Meta:
				model = Communitie
				fields = (
						'id',
						'name',
						'get_image',
						'get_absolute_url'
					)


class CategorySerializer(serializers.ModelSerializer):
		communities = CommunitieSerializer(many=True)

		class Meta:
				model = Category
				fields = (
						'id',
						'name',
						'get_absolute_url',
						'communities'
					)


class CategoriesSerializer(serializers.ModelSerializer):
		class Meta:
				model = Category
				fields = (
						'id',
						'name',
						'get_absolute_url',
					)


class CommunitieDetailSerializer(serializers.ModelSerializer):
		class Meta:
				model = Communitie
				fields = (
						'id',
						'name',
						'category',
						'get_image',
						'get_absolute_url',
						'slug',
						'description'
					)
