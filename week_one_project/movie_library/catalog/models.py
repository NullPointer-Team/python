from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=200)
    rating = models.CharField(max_length=10)
    year = models.CharField(max_length=5)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('movie-detail', args=[str(self.id)])
