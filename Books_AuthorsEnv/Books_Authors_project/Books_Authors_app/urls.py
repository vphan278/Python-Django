from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('books/create', views.add_item_to_inventory),
    path('authors/create', views.add_author),
]