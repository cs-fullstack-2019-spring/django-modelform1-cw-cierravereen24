from django.db import models
from django.utils import timezone


# Create your models here.
# a function that enables the user to enter information
class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    text = models.CharField(max_length=100000)
    created_date = models.DateTimeField(default=timezone.now)

    # makes the title your entry in the admin page
    def __str__(self):
        return self.title
