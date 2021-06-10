from django.db import models
from django.contrib.auth.models import User
from communitie.models import Communitie


class MyUser(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	communities = models.ManyToManyField(Communitie)

	def __str__(self):
		return self.user.username
