from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Preference(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    genres = models.CharField(max_length=50,
                              choices=[("Action", "Action"), ("Thriller", "Thriller"), ("Sci-Fi", "Sci-Fi"),
                                       ("War", "War"), ("Drama", "Drama"), ("Crime", "Crime")])

    def __str__(self):
        return '{} Preference'.format(self.user.username)

    def get_absolute_url(self):
        return reverse('blog-home')
