from django.db import models
from django.contrib.auth.models import User
from communitie.models import Communitie
from myuser.models import MyUser
from django.conf import settings


class Post(models.Model):
		user = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
		communitie = models.ForeignKey(Communitie, related_name='groups', on_delete=models.CASCADE, blank=True, null=True)
		title = models.CharField(max_length=300)
		post_text = models.TextField()
		#image = models.ImageField(upload_to='uploads/', blank=True, null=True)
		date = models.DateTimeField(auto_now_add=True)
		image_url = models.CharField(max_length=350, blank=True, null=True)

		class Meta:
				ordering = ('-date',)

		def __str__(self):
				return self.title

		def get_image(self):
			if(self.image_url):
					return self.image_url
			return None

		def get_user(self):
				return self.user.username

		def get_communitie(self):
				if(self.communitie):
						return self.communitie.slug
				return ''

		def get_reaction(self):
			try:
				reaction = Reaction.objects.get(user=self.user, post=self.pk) 
			except Exception:
				return None

			if reaction.reaction == True:
				return True
			elif reaction.reaction == False:
				return False

		def get_likes(self):
				reactions = Reaction.objects.filter(post=self.pk, reaction=True) 
				return len(reactions)

		def get_dislikes(self):
				reactions = Reaction.objects.filter(post=self.pk, reaction=False) 
				return len(reactions)

		def get_num_comments(self):
				comments = Comment.objects.filter(post=self.pk)
				return len(comments)

		def get_comments(self):
				comments = Comment.objects.filter(post=self.pk)
				return comments

		def get_communitie_url(self):
			if self.communitie:
					communitie = Communitie.objects.get(pk=self.communitie.id)
					return communitie.get_absolute_url()
			return None

		def get_description(self):
			if self.image_url:
				if len(self.post_text) > 200:
					return self.post_text[:200] + '...'
				else:
					return self.post_text[:200]

			elif len(self.post_text) > 500:
				return self.post_text[:500] + '...'
			else:
				return self.post_text

		def get_user_image(self):
			user = MyUser.objects.get(user=self.user)
			return user.get_profile_image()


class Reaction(models.Model):
	user = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)
	post = models.ForeignKey(Post, related_name='post', on_delete=models.CASCADE)
	reaction = models.BooleanField(blank=True, null=True)

	def __str__(self):
		return f'{self.user.username} {self.reaction} on "{self.post.title}"'


class Comment(models.Model):
	user = models.ForeignKey(User, related_name='comments_post', on_delete=models.CASCADE)
	post = models.ForeignKey(Post, related_name='post_comment', on_delete=models.CASCADE)
	comment = models.TextField()
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f'{self.user.username} on "{self.post.title}"'

	class Meta:
		ordering = ('-date',)

	def get_user(self):
		return self.user.username

	def get_user_image(self):
			user = MyUser.objects.get(user=self.user)
			return user.get_profile_image()
