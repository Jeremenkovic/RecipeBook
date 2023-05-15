from django.test import TestCase
from .models import Recipe, Tag
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

class RecipeModelTest(TestCase):
    def setUp(self):
        self.recipe = Recipe.objects.create(
            title="Spaghetti Bolognese",
            ingredients="Spaghetti, Minced meat, Tomatoes",
            preparation="Boil spaghetti. Cook meat with tomatoes. Mix together.",
            cook_time=30
        )
    
    def test_recipe_creation(self):
        self.assertTrue(isinstance(self.recipe, Recipe))
        self.assertEqual(self.recipe.__str__(), self.recipe.title)

class TagModelTest(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(
            name="Italian",
        )
    
    def test_tag_creation(self):
        self.assertTrue(isinstance(self.tag, Tag))
        self.assertEqual(self.tag.__str__(), self.tag.name)


class RecipeAPITest(APITestCase):
    def test_list_recipes(self):
        Recipe.objects.create(title="Spaghetti Bolognese", ingredients="Spaghetti, Minced meat, Tomatoes", preparation="Boil spaghetti. Cook meat with tomatoes. Mix together.", cook_time=30)
        response = self.client.get(reverse('recipe-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

class TagAPITest(APITestCase):
    def test_list_tags(self):
        Tag.objects.create(name="Italian")
        response = self.client.get(reverse('tag-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)