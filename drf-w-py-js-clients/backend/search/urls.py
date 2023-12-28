from django.urls import path
from . import views

urlpatterns = [
    path("algolia", views.search_list_algolia, name="search-algolia"),
    path("", views.search_list_django, name="search-django"),
]
