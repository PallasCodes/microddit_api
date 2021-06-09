from django.urls import path, include

from communitie import views


urlpatterns = [
	path('categories/', views.CategoriesList.as_view()),
	path('category/<slug:category_slug>/', views.CategoryDetails.as_view()),
	path('<slug:category_slug>/<slug:communitie_slug>/', views.CommunitieDetail.as_view()),
]
