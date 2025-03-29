from django.urls import path
from .views import search_articles

urlpatterns = [
    path("news/search/", search_articles, name="search_articles"),
]