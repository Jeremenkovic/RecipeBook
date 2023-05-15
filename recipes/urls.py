from django.urls import path
from . import views

urlpatterns = [
    path('recipes/', views.RecipeListCreate.as_view(), name='recipe_list_create'),
    path('recipes/<int:pk>/', views.RecipeUpdateDelete.as_view(), name='recipe_update_delete'),
    path('tags/', views.TagListCreate.as_view(), name='tag_list_create'),
]
