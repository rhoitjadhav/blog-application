# Packages
from django.urls import path

# Modules
from . import views

urlpatterns = [
    path('', views.posts, name='posts'),
    path('upload-image', views.upload_image, name='upload_image'),
]
