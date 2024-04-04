from django.db import models

# Create your models here.
from song_recommendation.models import Artist
from django.contrib.auth.models import User as DjangoUser

class UserPreferences(models.Model):
    user = models.ForeignKey(DjangoUser, on_delete=models.CASCADE)
    artist_id = models.ForeignKey(Artist,max_length=45, null=True, on_delete=models.CASCADE)
    class Meta:
        db_table = "user_preferences"

    def __str__(self):
        return f"{self.user.username}'s Preferences"

class UserEmotionData(models.Model):
    analysis_id = models.CharField(max_length=45, primary_key=True)
    user = models.ForeignKey(DjangoUser, on_delete=models.CASCADE)
    emotion = models.CharField(max_length=45, null=True)
    class Meta:
        db_table = "user_emotion_data"
    def __str__(self):
        return f"{self.user.username}'s Emotion Data"
