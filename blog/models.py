from django.db import models

# Create your models here.
class BlogModel(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=50)
    body = models.TextField()
    
    def __str__(self):
        return self.title + ' | ' + str(self.author)
    