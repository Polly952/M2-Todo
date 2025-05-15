from django.db import models

# Create your models here.

class TodoappModel(models.Model):
    task = models.CharField(max_length=200)
    notes = models.TextField()
    completed = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    