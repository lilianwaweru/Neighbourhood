from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Neighbourhood(models.Model):
    name = models.CharField(max_length = 20)
    location = models.CharField(max_length =20)
    occupants = models.IntegerField(default=0)
    image = models.ImageField(upload_to = 'images/',blank=True)
    neighbour_user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    def save_Neighbourhood(self):
        self.save()

    def delete_Neighbourhood(self):
        self.delete()

    def update_Neighbourhood(self,location):
        self.location = location
        self.save()


    def __str__(self):
        return self.location




class Profile(models.Model):
    profile_picture = models.ImageField(upload_to = 'images/',blank=True)
    bio = models.CharField(max_length = 70)
    contact = models.CharField(max_length=12)
    user_prof = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    neighbourhood = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE,null=True)


    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def update_bio(self,bio):
        self.bio = bio
        self.save()


    def __str__(self):
        return f'{Profile}'

class Business(models.Model):
    business_name = models.CharField(max_length = 20)
    business_email = models.CharField(max_length = 20)
    description = models.TextField(max_length=300,default=0)
    contact = models.CharField(max_length=12)
    business_image = models.ImageField(upload_to = 'images/',blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    neighbourhood = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE,null=True)


    def create_business(self):
        self.create()

    def delete_business(self):
        self.delete()

    def update_business(self,business):
        self.business = business
        self.update()

class Post(models.Model):
    title = models.CharField(max_length = 70)
    email = models.CharField(max_length = 20)
    description = models.TextField(max_length=300,default=0)
    contact = models.CharField(max_length = 12)
    post_user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    neighbourhood = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE,null=True)
