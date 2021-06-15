from django.urls import path, include

from myuser import views


urlpatterns = [
	path('user/follow/', views.follow_or_unfollow),
	path('user/search/<str:query>/', views.SearchUser.as_view()),
	path('user/get-followed/', views.get_followed),
	path('user/update/', views.update_profile),
	path('user/<str:username>/', views.MyUserDetail.as_view()),
	path('profile/create/', views.create_profile),
]