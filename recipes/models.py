from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    ingredients = models.TextField()
    instructions = models.TextField()
    cook_time = models.PositiveIntegerField()
    tags = models.ManyToManyField('Tag', blank=True)

    def __str__(self):
        return self.title

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
