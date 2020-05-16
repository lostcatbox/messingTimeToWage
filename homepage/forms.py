from django import forms
from .models import *
class HomePageForm(forms.ModelForm):
    class Meta:
        model = MessingData
        fields = ('today_playingtime','today_messingtime', 'eating_time', 'other_time')