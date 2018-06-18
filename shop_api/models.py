from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Item(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='Images')
    owner = models.ForeignKey(User, related_name="items",on_delete=models.PROTECT, null=True)



    def __str__(self):
        return self.title


class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    

"""class User(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    # password = models.CharField(min_length=8)
    # username = models.CharField(max_Length=50)

    def __str__(self):
        return self.username"""



class Rating(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ManyToManyField(User)
    item = models.ManyToManyField(Item)
    rating = models.IntegerField()


    def __str__(self):
        return self.user