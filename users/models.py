from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from multiselectfield import MultiSelectField


class Preference(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    genres = MultiSelectField(choices=[("Action", "Action"), ("Thriller", "Thriller"), ("Sci-Fi", "Sci-Fi"),
                                       ("War", "War")])

    def __str__(self):
        return '{} Preference'.format(self.user.username)

    def get_absolute_url(self):
        return reverse('blog-home')
