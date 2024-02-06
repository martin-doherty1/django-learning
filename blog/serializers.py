from django.contrib.auth.models import User
from rest_framework import serializers

from blog.models import Article, Category


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "first_name", "last_name")


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'description']

    def validate_name(self, value):
        if not (value and value.strip()):
            raise serializers.ValidationError("Name must be not be blank or null")
        return value

    def validate_description(self, value):
        if not (value and value.strip()):
            raise serializers.ValidationError("Description must be not be blank or null")
        return value


class ArticleSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    categories = CategorySerializer(many=True)

    class Meta:
        model = Article
        fields = "__all__"