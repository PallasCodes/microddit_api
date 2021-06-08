from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):
		class Meta:
				model = Post
				fields = (
						'id',
						'title',
						'post_text',
						'get_image',
						'date',
						'get_user',
					)

class CreatePostSerializer(serializers.ModelSerializer):
			class Meta:
					model = Post
					fields = (
							'id',
							'title',
							'post_text',
							'image',
							'date',
							'get_user'
						)
