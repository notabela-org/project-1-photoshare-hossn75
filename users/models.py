from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    image = models.ImageField(default = 'default.jpg', upload_to = "profile_pics")
    bio = models.CharField(max_length=100)

    
    def __str__(self):
        return self.profile.user


class Post(models.Model):
    image = models.ImageField(upload_to ='photoshare/media')
    puser = models.ForeignKey('Profile', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, null= True)
    description_field = models.CharField(max_length = 150, null = True)

    def __str__(self):
        return self.post.puser

class Comment(models.Model):
     description_field = models.CharField(max_length = 150, null = True )
     post = models.CharField(max_length = 200)
     cuser = models.ForeignKey('Profile', on_delete=models.CASCADE, null = True)
     date = models.DateTimeField(auto_now_add=True)

    


   