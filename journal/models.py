
from django.db import models
from django.contrib.auth.models import User


class Entry(models.Model):
    MOOD_CHOICES = [
        ('happy', 'Happy'),
        ('sad', 'Sad'),
        ('neutral', 'Neutral'),
        ('anxious', 'Anxious'),
        ('excited', 'Excited'),
    ]

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='entries'
    )

    category = models.ForeignKey(
        'categories.Category',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='entries'
    )

    title = models.CharField(max_length=200)
    content = models.TextField()
    mood = models.CharField(
        max_length=10,
        choices=MOOD_CHOICES,
        default='neutral'
    )
    is_private = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.owner.username})"

