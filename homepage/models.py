from django.db import models
from django.core.exceptions import ValidationError

def validate_time(value):
    if (value<0)or(value>24):
        message = u"0~24사이의 값만 입력할수있습니다"
        raise ValidationError(message)

class MessingData(models.Model):
    today_playingtime = models.IntegerField(verbose_name="오늘 공부랑", validators=[validate_time])
    today_messingtime = models.IntegerField(verbose_name="오늘 딴짓량", validators=[validate_time])
    sleeping_time = models.IntegerField(default=8, verbose_name="잠든 시간", validators=[validate_time])
    eating_time = models.IntegerField(default=2, verbose_name="밥 먹은 시간", validators=[validate_time])
    other_time = models.IntegerField(default=0, verbose_name="기타 딴짓 시간", validators=[validate_time])

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Create your models here.
