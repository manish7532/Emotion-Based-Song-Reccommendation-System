from django import forms
# from song_recommendation.models import Artist
# from .models import UserPreferences
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from django.utils.safestring import mark_safe


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    # forms.py


# forms.py



# class ArtistCheckboxSelectMultiple(forms.CheckboxSelectMultiple):
#     template_name = "widgets/artist_checkbox_select.html"


# class RegistrationForm(UserCreationForm):
#     artist_preferences = forms.ModelMultipleChoiceField(
#         queryset=Artist.objects.all(),
#         widget=ArtistCheckboxSelectMultiple,
#         required=False,
#     )

#     class Meta:
#         model = User
#         fields = ("username", "password1", "password2", "artist_preferences")


# class ArtistCheckboxSelectMultiple(forms.CheckboxSelectMultiple):
#     def render(self, name, value, attrs=None, renderer=None):
#         output = super().render(name, value, attrs, renderer)
#         model = self.choices.field.queryset.model
#         images = [
#             f'<img src="{artist.artist_image_url}" alt="{artist.artist_name}">'
#             for artist in model.objects.all()
#         ]
#         return mark_safe(output + "<br>".join(images))


# class UserPreferencesForm(forms.Form):
#     artists = forms.ModelMultipleChoiceField(
#         queryset=Artist.objects.all(),
#         widget=ArtistCheckboxSelectMultiple,
#     )
