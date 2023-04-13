from django.db import models

# Create your models here.
class S_l(models.Model):
    full_link=models.CharField(max_length=200)
    short_link=models.CharField(max_length=6)
    def __str__(self):
        return self.full_link
