# Packages
from django.urls import path

# Modules
from . import views

urlpatterns = [
    path('follower', views.follower, name='follower'),
    path('following', views.following, name='following'),
]
