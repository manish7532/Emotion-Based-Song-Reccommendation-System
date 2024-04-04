from django.contrib import admin
from .models import UserPreferences, UserEmotionData
# Register your models here.
admin.site.register(UserPreferences)
admin.site.register(UserEmotionData)