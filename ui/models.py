from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    CATEGORIES_CHOICES = (
        ('hobby', 'Hobby'),
        ('business', 'Business'),
        ('romance', 'Romance'),
        ('other', 'Other')
    )
    title = models.CharField(max_length=50)
    body = models.TextField()
    category = models.CharField(max_length=40, choices=CATEGORIES_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}: {self.title} -- {self.body}"
