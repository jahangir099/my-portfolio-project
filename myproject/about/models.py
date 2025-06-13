from django.db import models

# Create your models here.


class About(models.Model):
    name = models.CharField(max_length=100)
    short_intro = models.CharField(max_length=255)
    bio = models.TextField()
    photo = models.ImageField(upload_to='about/', null=True, blank=True)

    def __str__(self):
        return self.name
