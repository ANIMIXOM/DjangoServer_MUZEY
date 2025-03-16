from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver


class GameResult(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='game_results')
    score = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.score} - {self.date}"

    @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    def create_game_result(sender, instance, created, **kwargs):
        if created:
            GameResult.objects.create(user=instance)
