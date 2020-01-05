from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    rating = models.FloatField()
    storyline = models.TextField()
    genres = models.CharField(choices=[("Action", "Action"), ("Thriller", "Thriller"), ("Sci-Fi", "Sci-Fi"),
                                       ("War", "War"), ("Romance", "Romance"), ("Drama", "Drama")], default="Action",
                              max_length=50)
    upvote = models.IntegerField(default=0)
    downvote = models.IntegerField(default=0)
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Review(models.Model):
    content = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return reverse('blog-home')
