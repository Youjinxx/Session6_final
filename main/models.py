from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    writer = models.TextField(max_length=100)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to="blog/", blank=True, null=True)
    
    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:20]
    
    