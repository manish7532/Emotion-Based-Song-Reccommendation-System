
from django.contrib import admin
from django.urls import path
from .views import capture_image, capture_image_page
# from django.contrib.auth import views as auth_views
app_name = "emotion_detection"

urlpatterns = [
    path('capture_image/', capture_image, name='capture_image'),
    path('capture/', capture_image_page, name='capture_image_page'),
]
