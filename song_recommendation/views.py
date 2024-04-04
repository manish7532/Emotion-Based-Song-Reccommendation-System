from random import sample
from django.shortcuts import render
# from django.db import connection
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import *
from user_management.models import UserPreferences

def index(request):
    return render(request, "index.html")

@login_required
def home(request, emotion):
    user_id = request.user.id

    # Step 1: Fetch artist_ids associated with the given user_id from user_preferences table
    user_preferences = UserPreferences.objects.filter(user_id=user_id).values_list(
        "artist_id", flat=True
    )

    # Step 2: Fetch song_ids associated with the fetched artist_ids from song_artist table
    song_artist_ids = SongArtist.objects.filter(
        artist_id__in=user_preferences
    ).values_list("song_id", flat=True)

    # Step 3: Fetch song_ids that have emotion as 'happy' from song_emotion table
    happy_song_ids = SongEmotion.objects.filter(
        emotion=emotion, song_id__in=song_artist_ids
    ).values_list("song_id", flat=True)
    # Step 4: Fetch titles of the remaining song_ids from the song table, sorted by popularity
    # Get the top songs by popularity
    top_song_ids = (
        Song.objects.filter(song_id__in=happy_song_ids)
        .values_list("song_id", flat=True)
        .order_by("-popularity")
    )

    # If there are more than 5 songs, randomly select 5 songs
    if len(top_song_ids) > 5:
        random_happy_song_ids = sample(list(top_song_ids), 10)
    else:
        random_happy_song_ids = top_song_ids

    context = {
        "track_ids": random_happy_song_ids,
        "emotions": emotion.capitalize(),
        "user_id": user_id,
    }
    return render(request, "play_track.html", context=context)


# @login_required
# def home(request, emotion):
#         # Assuming you have a function to get recommended songs based on emotions
#     # Replace this with your actual logic to get recommended songs
#     matching_song_ids = SongEmotion.objects.filter(emotion=emotion).values_list('song_id', flat=True)[:5]
#     user_id = request.user.id

#         # return Song.objects.values_list('song_id', flat=True)[:5]

#     context = {
#         "track_ids": matching_song_ids,
#         "emotions": emotion.capitalize(),
#         "user_id" : user_id,
#     }
#     return render(request, 'play_track.html', context=context)
