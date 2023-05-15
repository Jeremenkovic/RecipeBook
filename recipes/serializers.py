from rest_framework import serializers
from .models import Recipe, Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name']

class RecipeSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = Recipe
        fields = ['title', 'ingredients', 'instructions', 'cook_time', 'tags']
