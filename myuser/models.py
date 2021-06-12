from django.db import models
from django.contrib.auth.models import User
from communitie.models import Communitie


class MyUser(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=35, blank=True, null=True)
	profile_image = models.ImageField(upload_to='uploads/', default='uploads/default.png')
	cover_image = models.ImageField(upload_to='uploads/', blank=True, null=True)
	bio_description = models.TextField(blank=True, null=True)
	communities = models.ManyToManyField(Communitie, blank=True)
	friends = models.ManyToManyField(User, related_name="added_friends", blank=True)

	def __str__(self):
		return self.user.username

	def get_profile_image(self):
		if(self.profile_image):
			return 'http://127.0.0.1:8000' + self.profile_image.url
		return None

	def get_cover_image(self):
		if(self.cover_image):
			return 'http://127.0.0.1:8000' + self.cover_image.url
		return None

	def get_username(self):
		return self.user.username
