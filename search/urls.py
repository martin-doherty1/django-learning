# search/urls.py

from django.urls import path

from search.views import SearchArticles, SearchCategories, SearchUsers, SearchExercises

urlpatterns = [
    path("user/<str:query>/", SearchUsers.as_view()),
    path("category/<str:query>/", SearchCategories.as_view()),
    path("article/<str:query>/", SearchArticles.as_view()),
    path("exercise/<str:query>/", SearchExercises.as_view())
]