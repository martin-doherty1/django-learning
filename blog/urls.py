from django.urls import path, include
from rest_framework import routers
from blog.views import UserViewSet, CategoryViewSet, ArticleViewSet

router = routers.DefaultRouter()
router.register("users", UserViewSet, "user")
router.register("categories", CategoryViewSet, "category")
router.register("articles", ArticleViewSet, "article")

urlpatterns = [
    path("", include(router.urls)),
]
