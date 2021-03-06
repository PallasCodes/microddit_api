from django.db import models
from django.conf import settings


class Category(models.Model):
		name = models.CharField(max_length=30)
		slug = models.SlugField()

		class Meta:
				ordering = ('name',)

		def __str__(self):
				return self.name

		def get_absolute_url(self):
				return f'/{self.slug}/'


class Communitie(models.Model):
		name = models.CharField(max_length=50)
		description = models.TextField()
		#image = models.ImageField(upload_to='uploads/')
		slug = models.SlugField()
		category = models.ForeignKey(Category, related_name="communities", on_delete=models.CASCADE, default=1)
		num_members = models.IntegerField(default=0)
		icon = models.CharField(max_length=50, null=True, blank=True)
		image_url = models.CharField(max_length=200, default="")

		class Meta:
				ordering = ('name',)

		def __str__(self):
				return self.name

		def get_image(self):
				return self.image_url

		def get_absolute_url(self):
				return f'/{self.category.slug}/{self.slug}/'

		def get_category(self):
				return self.category.name

		def increase_members(self):
				self.num_members += 1

		def decrease_members(self):
				self.num_members -= 1
