from django.db import models


# Create your models here.
class TODOLIST(models.Model):
    Work = models.CharField(max_length = 200)
    Time = models.TextField(max_length = 40)
    status = models.BooleanField(default = False)


    def __str__(self):
        return self.Work


