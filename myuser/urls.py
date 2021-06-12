from django.urls import path, include

from myuser import views


urlpatterns = [
	path('user/<str:username>/', views.MyUserDetail.as_view()),
]