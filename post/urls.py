from django.urls import path, include

from post import views


urlpatterns = [
		path('public-feed/', views.PublicFeed.as_view()),
		path('posts/', views.Posts.as_view()),
		path('posts/react/', views.react_to_post),
		path('posts/<int:communitie_pk>/', views.PostsFromCommunitie.as_view()),
]
