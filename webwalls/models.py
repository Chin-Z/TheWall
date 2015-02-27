from django.db import models

# Create your models here.

class Message(models.Model):
    body = models.TextField()
    create_time = models.DateTimeField()

    def __str__(self):
        return self.body
