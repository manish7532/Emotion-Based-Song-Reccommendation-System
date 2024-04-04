from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.user_login, name="login"),
    path("signup/", views.user_signup, name="signup"),
    path("logout/", views.user_logout, name="logout"),
    path("user_preference/", views.artist_list, name="artist_list"),
    # path("user_preferences", views.set_user_preferences, name="set_user_preferences"),
    path(
        "user_preference/<int:user_id>/",
        views.artist_list,
        name="artist_list_with_user",
    ),
]
