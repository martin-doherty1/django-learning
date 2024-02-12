from django.test import TestCase
from rest_framework.reverse import reverse
from blog.models import Category


# Create your tests here.
def create_category(category_name, category_description):
    return Category.objects.create(name=category_name, description=category_description)


class ArticleTests(TestCase):
    def test_no_articles(self):
        """
        If no questions exist, an appropriate message is displayed.
        """
        print(reverse("article-list"))
        response = self.client.get(reverse("article-list"))
        self.assertEqual(response.status_code, 200)


class CategoryTests(TestCase):

    def test_with_one_category(self):
        category = create_category(category_name="Winner", category_description="pool")
        data = {"pk": category.id}
        response = self.client.get(reverse("category-detail", kwargs=data))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["name"], category.name)
        self.assertEqual(response.data["description"], category.description)

    def test_category_post(self):
        data = {'name': "testPost", 'description': "testPost"}
        response = self.client.post(reverse("category-list"), data)
        self.assertEqual(Category.objects.last().name, data["name"])
        self.assertEqual(response.status_code, 201)
