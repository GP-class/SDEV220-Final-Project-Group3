from django.db import models
from members.models import Member
from games.models import Game


class Score(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    score = models.IntegerField()
    
    def __str__(self):
        return f"{self.member.full_name}: {self.score}"