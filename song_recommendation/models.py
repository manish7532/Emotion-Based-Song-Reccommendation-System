"""Song Recommendation Models"""
from django.db import models

# Create your models here.

class Artist(models.Model):
    """Artist Table"""
    artist_id = models.CharField(max_length=45, primary_key=True)
    artist_name = models.CharField(max_length=45)
    artist_image_url = models.CharField(max_length=255)
    artist_popularity = models.IntegerField(default=0)
    class Meta:
        db_table = 'artist'

class Album(models.Model):
    """Album Table"""
    album_id = models.CharField(max_length=45, primary_key=True)
    album_name = models.CharField(max_length=45, null=True)
    class Meta:
        db_table = 'album'

class Song(models.Model):
    """Song Table"""
    song_id = models.CharField(max_length=45, primary_key=True)
    title = models.CharField(max_length=45)
    popularity = models.IntegerField(default=0)
    class Meta:
        db_table = 'song'

class SongEmotion(models.Model):
    """SongEmotion Table"""
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE, db_column="song_id")
    emotion = models.CharField(max_length=45)
    class Meta:
        """Table MetaData"""
        unique_together = ('song_id', 'emotion')
        db_table = "song_emotion"


class SongArtist(models.Model):
    """SongArtist Table"""

    song_id = models.ForeignKey(Song, on_delete=models.CASCADE, db_column="song_id")
    artist_id = models.ForeignKey(Artist, on_delete=models.CASCADE, db_column="artist_id")
    class Meta:
        """Table MetaData"""
        unique_together = ('song_id', 'artist_id')
        db_table = "song_artist"