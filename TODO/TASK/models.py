from django.db import models


class Task(models.Model):

    completed = models.BooleanField(default=False)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=200,blank=True)






