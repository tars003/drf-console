from django.urls import path, include
from . import views

urlpatterns = [
    path('/category', views.CategoryView),
    path('/add_article', views.add_article),

]
