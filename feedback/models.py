from django.db import models
from blog.models import BlogModel

# Create your models here.


class Feedback(models.Model):
    blog_name=models.ForeignKey(BlogModel,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    comment = models.CharField(max_length=300)

    def __str__(self):
        return self.name

# class FeedbackModel(models.Model):
#     # blog_name=models.ForeignKey(BlogModel,on_delete=models.CASCADE)
#     name=models.CharField(max_length=100)
#     email=models.EmailField()
#     comment=models.CharField(max_length=100)
    
#     def __str__(self):
#         return self.name

