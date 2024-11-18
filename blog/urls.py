from django.urls import path
from . import views


urlpatterns = [
  path("blog",views.blog, name="blog"),
  path("blog/categoria/<categoria_id>/", views.categoria, name="categoria")


    
]