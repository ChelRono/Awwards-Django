from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_picture =CloudinaryField('picture' ,null='True')
    bio = models.TextField(max_length=500, default="My Bio", blank=True)
    
   


    def __str__(self):
        return f'{self.user.username} Profile'
