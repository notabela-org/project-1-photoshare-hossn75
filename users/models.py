from django.db import models
from django.contrib.auth.models import User

#Importing date method
import datetime

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    image = models.ImageField(upload_to ='',default='/default.jpg', blank= True)
    bio = models.CharField(max_length=350)

    def get_bio(self):
        return self.bio

    def get_image(self):
        return self.image

class Post(models.Model):

    image = models.ImageField(upload_to ='Posts/')
    caption = models.CharField(max_length=700)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, null = True)

class Comment(models.Model):

    comment = models.CharField(max_length=350)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
