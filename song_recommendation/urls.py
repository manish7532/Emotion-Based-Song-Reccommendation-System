
from django.urls import path
from .views import home, index

app_name = 'song_recommendation'

urlpatterns = [
    path("", index, name="index"),
    path("<str:emotion>", home, name="home"),
]