from django.test import TestCase
from rest_framework.reverse import reverse

from blog.tests import create_category
from gym.tests import create_exercise


# Create your tests here.

class SearchTests(TestCase):

    def setUp(self):
        create_category(category_name="test_category", category_description="testing 123")
        create_exercise("row", "back", "rowing on the river", "BW")

    def test_search_category(self):
        response = self.client.get(reverse("categorySearch", args=["test_category"]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['results'][0]["name"], "test_category")
        self.assertEqual(response.data['results'][0]["description"], "testing 123")

    def test_search_exercise(self):
        response = self.client.get(reverse("exerciseSearch", args=["row"]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['results'][0]["description"], "rowing on the river")

    def test_exerciseType_search(self):
        response = self.client.get(reverse("exerciseTypesSearch"))
        self.assertEqual(response.status_code, 200)
        self.assertGreater(len(response.data['results']), 0)
