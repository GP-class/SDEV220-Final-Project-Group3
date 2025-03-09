from django.db import models
from members.models import Member

class Game(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=200)
    participants = models.ManyToManyField(Member, through='Score')
    
    def __str__(self):
        return f"Game on {self.date} at {self.location}"