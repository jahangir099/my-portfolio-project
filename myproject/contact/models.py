from django.db import models

# Create your models here.

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)  # 👉 eta new field
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name
