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

