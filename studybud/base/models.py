from django.db import models

class Room(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return self.name