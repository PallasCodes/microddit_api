from rest_framework import serializers

from .models import MyUser


class MyUserSerializer(serializers.ModelSerializer):	
	class Meta:
		model = MyUser
		fields = (
				'id',
				'get_username',
				'get_profile_image',
				'get_cover_image',
				'bio_description',
				'name'
			)
