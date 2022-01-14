from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.TextField()
    status = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'book'
         