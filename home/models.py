from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import datetime
 


# Create your models here.
class Post(models.Model) :

    title = models.CharField(max_length=150)
    content = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now())
    posted_by = models.ForeignKey(User,on_delete=models.CASCADE)
    # timestamp is used as generic name for posted on and account created on fields...Keep this as a practice
    # posted_by is a foreign key that refers to author username in Author table 
    # When a author is removed from Author table all his posts are to be deleted
    def __str__(self) :
        return self.title+" by "+str(self.posted_by) 

class Contact(models.Model) :

    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now())

    def __str__(self) :
        return self.name 

    