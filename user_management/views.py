from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from song_recommendation.models import Artist
from .models import UserPreferences
from .forms import SignupForm, LoginForm

# Create your views here.


# signup page
def user_signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("artist_list_with_user", user_id=request.user.id)
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = SignupForm()

    return render(request, "register.html", {"form": form})


# def user_signup(request):
#     if request.method == "POST":
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             user = form.save()

#             # Log in the user
#             login(request, user)

#             # Redirect to artist_list, passing the user instance
#             return redirect("artist_list_with_user", user_id=request.user.id)
#     else:
#         form = SignupForm()
#     return render(request, "register.html", {"form": form})


# login page
def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect("emotion_detection:capture_image")
            else:
                messages.error(request, "Authentication failed")
                return render(
                    request,
                    "login.html",
                    {
                        "form": form,
                        "custom_error": "Username and Password didn't match. Please try again.",
                    },
                )
        else:
            messages.error(request, "Invalid form data. Please check your inputs.")
    else:
        form = LoginForm()

    return render(request, "login.html", {"form": form})


# def user_login(request):
#     if request.method == "POST":
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data["username"]
#             password = form.cleaned_data["password"]
#             user = authenticate(request, username=username, password=password)
#             if user:
#                 login(request, user)
#                 return redirect("emotion_detection:capture_image_page")
#     else:
#         form = LoginForm()
#     return render(request, "login.html", {"form": form})


# logout page
def user_logout(request):
    logout(request)
    return redirect("login")


@login_required
def artist_list(request, user_id=None):
    if user_id is not None:
        user = get_object_or_404(User, id=user_id)
    else:
        user = request.user

    # Rest of your code...
    artists = Artist.objects.all().order_by("-artist_popularity")
    # Paginate the artists
    paginator = Paginator(artists, 6)  # Show 6 artists per page

    page = request.GET.get("page")
    try:
        artists = paginator.page(page)
    except PageNotAnInteger:
        artists = paginator.page(1)
    except EmptyPage:
        artists = paginator.page(paginator.num_pages)
    if request.method == "POST":
        # Handle form submission here
        selected_artist_ids = request.POST.getlist("selected_artists")
        selected_artists = Artist.objects.filter(artist_id__in=selected_artist_ids)

        # Create UserPreferences for the current user and selected artists
        for artist in selected_artists:
            UserPreferences.objects.create(user=user, artist_id=artist)

        return redirect("login")

    context = {
        "artists": artists,
    }

    return render(request, "artist.html", context)


# def artist_list(request):
#     artists = Artist.objects.all().order_by("-artist_popularity")

#     # Paginate the artists
#     paginator = Paginator(artists, 6)  # Show 6 artists per page

#     page = request.GET.get("page")
#     try:
#         artists = paginator.page(page)
#     except PageNotAnInteger:
#         artists = paginator.page(1)
#     except EmptyPage:
#         artists = paginator.page(paginator.num_pages)

#     if request.method == "POST":
#         # Handle form submission here
#         selected_artist_ids = request.POST.getlist("selected_artists")
#         selected_artists = Artist.objects.filter(artist_id__in=selected_artist_ids)
#         # Do something with the selected artists
#         print(selected_artists)
#         for artist in selected_artists:
#             obj = UserPreferences(user=request.user, artist_id=artist)
#             obj.save()
#         return redirect("login")

#     context = {
#         "artists": artists,
#     }

#     return render(request, "artist.html", context)

# def user_signup(request):
#     if request.method == "POST":
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             user = form.save()

#             # Log in the user
#             login(request, user)

#             return redirect("artist_list", user_id=user.id)
#     else:
#         form = SignupForm()
#     return render(request, "register.html", {"form": form})
