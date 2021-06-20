from django.db import models
from django.contrib.auth.models import User
from communitie.models import Communitie
from django.conf import settings


class MyUser(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=35, blank=True, null=True)
	#profile_image = models.ImageField(upload_to='uploads/', default='uploads/default.png')
	#cover_image = models.ImageField(upload_to='uploads/', blank=True, null=True)
	bio_description = models.TextField(blank=True, null=True)
	communities = models.ManyToManyField(Communitie, blank=True)
	friends = models.ManyToManyField(User, related_name="added_friends", blank=True)
	profile_image_url = models.CharField(max_length=350, default='https://microddit-api.herokuapp.com/media/uploads/default.png')
	cover_image_url = models.CharField(max_length=350, blank=True, null=True)

	def __str__(self):
		return self.user.username

	def get_profile_image(self):
		if(self.profile_image_url):
			return self.profile_image_url
		return None

	def get_cover_image(self):
		if(self.cover_image_url):
			return self.cover_image_url
		return None

	def get_username(self):
		return self.user.username
