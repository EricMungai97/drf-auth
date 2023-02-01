from django.db import models
from django.contrib.auth import get_user_model


class Movie(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    Title = models.CharField(max_length=256)
    Director = models.TextField()
    Genre = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Title
