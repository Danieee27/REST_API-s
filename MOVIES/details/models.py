from django.db import models

# Create your models here.
class Detail(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField()
    release_date = models.DateField()
    streaming_platform = models.CharField(max_length = 100)
    rating = models.FloatField()

    def __str__(self):
        return self.title
