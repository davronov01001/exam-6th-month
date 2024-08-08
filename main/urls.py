from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('category/<int:category_id>', category, name='category'),
    path('picture/<int:picture_id>', picture, name='picture'),
]
