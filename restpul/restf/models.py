from django.db import models

# Create your models here.

class Article(models.Model):
    Title = models.CharField(max_length=100)
    Author = models.CharField(max_length=100)
    Email=models.EmailField()
    date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Title
