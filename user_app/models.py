from django.db import models

# Create your models here.

class UserInformation(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    mobile = models.CharField(max_length=100)
    role = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.username
