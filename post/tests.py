from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework import status

from .models import Post, Reaction, Comment
from myuser.models import MyUser


class PostTestCase(APITestCase):
	# SET UP
	def setUp(self):
		self.user = User.objects.create_user(username="test-user",password="testpw123")
		MyUser.objects.create(user=self.user,name="test-user")
		self.token = Token.objects.create(user=self.user)
		self.api_authentication()
		
	def api_authentication(self):
		self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)


	# POST TESTS
	def test_create_post_authenticated(self):
		data = {
			"title": "test title",
			"post_text": "lorem ipsum...",
			"communitie": "1",	
		}
		response = self.client.post("/api/v1/posts/", data)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

	def test_create_post_un_authenticated(self):
		data = {
			"title": "test title",
			"post_text": "lorem ipsum...",
			"communitie": "1",	
		}
		self.client.force_authenticate(user=None)
		response = self.client.post("/api/v1/posts/", data)
		self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

	def test_delete_post_authenticated(self):
		post = Post.objects.create(title='test title', post_text='uwuwuw', user_id=1)
		response = self.client.delete(f"/api/v1/posts/delete/{post.id}/")
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_delete_post_un_authenticated(self):
		post = Post.objects.create(title='test title', post_text='uwuwuw', user_id=1)
		self.client.force_authenticate(user=None)
		response = self.client.delete(f"/api/v1/posts/delete/{post.id}/")
		self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


	# REACTION TESTS
	def test_react_to_post_authenticated(self):
		post = Post.objects.create(title='test title', post_text='uwuwuw', user_id=1)
		data = {
			"post": post.id,
			"reaction": True
		}
		response = self.client.post("/api/v1/posts/react/", data)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

	def test_create_post_un_un_authenticated(self):
		post = Post.objects.create(title='test title', post_text='uwuwuw', user_id=1)
		data = {
			"post": post.id,
			"reaction": True
		}
		self.client.force_authenticate(user=None)
		response = self.client.post("/api/v1/posts/react/", data)
		self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


	# COMMENT TESTS
	def test_comment_post_authenticated(self):
		post = Post.objects.create(title='test title', post_text='uwuwuw', user_id=1)
		data = {
			"post": post.id,
			"comment": "test comment"
		}
		response = self.client.post("/api/v1/posts/comment/", data)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

	def test_comment_post_un_authenticated(self):
		post = Post.objects.create(title='test title', post_text='uwuwuw', user_id=1)
		data = {
			"post": post.id,
			"comment": "test comment"
		}
		self.client.force_authenticate(user=None)
		response = self.client.post("/api/v1/posts/comment/", data)
		self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
