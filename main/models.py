from django.core.exceptions import DisallowedHost
from django.contrib.auth.models import User
from django.db import connections, models
from PIL import Image
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    def __str__(self):
        return f'{self.user.username} Profile'
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
class Trades(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    coin = models.CharField(max_length=20)
    priceB = models.FloatField(blank=True, null=True)
    priceS = models.FloatField(blank=True, null=True)
    quantity = models.FloatField(blank=True, null=True)
    spent = models.FloatField(blank=True, null=True)
    test = models.FloatField(blank=True, null=True)
    class Meta:
        verbose_name_plural = 'trades'

    
    
