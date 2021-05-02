"""
app.recipe_users.urls
---------------------
Recipe users urls file
"""
from django.urls import path

from . import views

app_name = 'recipe_users'

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('token/', views.TokenApiView.as_view(), name='token'),
]
