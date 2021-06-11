from rest_framework import serializers

from .models import Post, Reaction


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
						'get_communitie',
					)


class AuthPostSerializer(serializers.ModelSerializer):
		class Meta:
				model = Post
				fields = (
						'id',
						'title',
						'post_text',
						'get_image',
						'date',
						'get_user',
						'get_communitie',
						'get_reaction',
						'get_likes',
						'get_dislikes',
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
							'get_user',
							'communitie',
						)


class ReactionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Reaction
		fields = (
			'post',
			'reaction'
		)