from django.core.exceptions import DisallowedHost
from django.db import DefaultConnectionProxy, models
   
class User(models.Model):
    username = models.CharField(max_length=30)
    def __str__(self):
        return self.username
class Trades(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    coin = models.CharField(max_length=10)
    profilePicture = models.ImageField(default='default.jpg', upload_to='profile_pics')
    
