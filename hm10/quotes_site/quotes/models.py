from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    fullname = models.CharField(max_length=255, unique=True)
    born_date = models.CharField(max_length=255, blank=True)
    born_location = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.fullname


class Quote(models.Model):
    text = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tags = models.CharField(max_length=255, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
