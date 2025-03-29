from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=255)
    link = models.URLField(unique=True)

    def __str__(self):
        return self.title