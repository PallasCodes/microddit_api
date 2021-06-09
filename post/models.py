from django.db import models
from django.contrib.auth.models import User
from communitie.models import Communitie


class Post(models.Model):
		user = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
		communitie = models.ForeignKey(Communitie, related_name='groups', on_delete=models.CASCADE, blank=True, null=True)
		title = models.CharField(max_length=300)
		post_text = models.TextField()
		image = models.ImageField(upload_to='uploads/', blank=True, null=True)
		date = models.DateTimeField(auto_now_add=True)

		class Meta:
				ordering = ('-date',)

		def __str__(self):
				return self.title

		def get_image(self):
			if(self.image):
					return 'http://127.0.0.1:8000' + self.image.url
			return ''

		def get_user(self):
				return self.user.username

		def get_communitie(self):
				if(self.communitie):
						return self.communitie.slug
				return ''
