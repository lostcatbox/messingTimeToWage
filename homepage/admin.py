from django.contrib import admin
from .models import *

class MessingDataAdmin(admin.ModelAdmin):
    model = MessingData
    list_display = ('today_playingtime','today_messingtime', 'eating_time', 'other_time', 'created_at', 'updated_at')

admin.site.register(MessingData, MessingDataAdmin)
# Register your models here.
