from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework import status

from .models import MyUser


class ProfileTestCase(APITestCase):
	# SET UP
	def setUp(self):
		self.user = User.objects.create_user(username="descartes",password="testpw123")
		MyUser.objects.create(user=self.user,name="descartes")
		self.token = Token.objects.create(user=self.user)
		self.api_authentication()

	def api_authentication(self):
		self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)


 	# PROFILE TESTS
	def test_create_profile(self):
		data = {
			"username": "rene",
		}
		user = User.objects.create_user(username="rene",password="testpw123")
		self.client.force_authenticate(user=user)
		response = self.client.post("/api/v1/profile/create/", data)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

	def test_follow_profile(self):
		data = {
			"username": "rene"
		}
		user = User.objects.create_user(username="rene",password="testpw123")
		response = self.client.post("/api/v1/user/follow/", data)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

	def test_follow_profile_unauthenticated(self):
		data = {
			"username": "rene"
		}
		user = User.objects.create_user(username="rene",password="testpw123")
		self.client.force_authenticate(user=None)
		response = self.client.post("/api/v1/user/follow/", data)
		self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

	def test_update_profile(self):
		data = {
			"name": "julio",
			"bio_description": "lorem ipsum"
		}
		response = self.client.put("/api/v1/user/update/", data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_update_profile_unauthenticated(self):
		data = {
			"name": "julio",
			"bio_description": "lorem ipsum"
		}
		self.client.force_authenticate(user=None)
		response = self.client.put("/api/v1/user/update/", data)
		self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)