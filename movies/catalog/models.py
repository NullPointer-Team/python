from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=200, help_text="enter a title name")
    year = models.CharField(max_length=4)
    rating = models.CharField(max_length=7)

    def __str__(self):
        return self.title
