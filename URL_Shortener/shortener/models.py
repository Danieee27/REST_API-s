from django.db import models
import shortuuid

# Create your models here.
class URL(models.Model):
    long_url = models.URLField(unique = True)
    short_code = models.CharField(max_length = 10, unique = True, blank = True)
    created_at = models.DateTimeField(auto_now_add = True)
    clicks = models.PositiveIntegerField(default = 0)
    
    #save method to generate short code
    def save(self, *args, **kwargs):
        if not self.short_code:
            self.short_code = shortuuid.uuid()[:6]
        super().save(*args, **kwargs)

    #name of object in admin
    def __str__(self):
        return f"{self.long_url} -> {self.short_code}"