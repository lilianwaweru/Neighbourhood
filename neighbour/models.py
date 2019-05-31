from django.db import models



# Create your models here.
class Profile(models.Model):
    profile_picture = models.ImageField(upload_to = 'images/',blank=True)
    bio = models.CharField(max_length = 70)
    contact = models.CharField(max_length=12)
    # project = models.ForeignKey('Project',on_delete=models.CASCADE,null=True)
    # user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def update_bio(self,bio):
        self.bio = bio
        self.save()


    def __str__(self):
        return f'{self.bio}'      
