from django.urls import path
from search.views import (SearchArticles, SearchCategories,
                          SearchUsers, SearchExercises, GetNumberOfTypes)

urlpatterns = [
    path("user/<str:query>/", SearchUsers.as_view()),
    path("category/<str:query>/", SearchCategories.as_view(), name="categorySearch"),
    path("article/<str:query>/", SearchArticles.as_view(), name="articleSearch"),
    path("exercise/<str:query>/", SearchExercises.as_view(), name="exerciseSearch"),
    path("exerciseTypes/", GetNumberOfTypes.as_view(), name="exerciseTypesSearch")
]
