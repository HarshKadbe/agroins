from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    username = models.CharField(max_length = 20)
    name = models.CharField(max_length = 50)
    email = models.EmailField(max_length = 100)
    location = models.CharField(max_length = 50, null=True, blank = True)
    password1 = models.CharField(max_length = 70)
    password2 = models.CharField(max_length = 70)
    
  
    
    
class PredictedData(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)
    nitrogen = models.CharField(max_length=30)
    phosphorus = models.CharField(max_length=30)
    pottasium = models.CharField(max_length=30)
    temperature = models.CharField(max_length=30)
    humidity = models.CharField(max_length=30)
    ph = models.CharField(max_length=30)
    rainfall = models.CharField(max_length=30)
    recommended_crop = models.CharField(max_length=30)
    prediction_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.recommended_crop
    
    
class PredictDisease(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)
    LeafImage = models.ImageField(upload_to='leafimages/')
    predicted_disease = models.CharField(max_length=30)
    prediction_date_leaf = models.DateTimeField(auto_now_add=True)
    
    # @property
    # def imageURL(self):
    #     try:
    #         url = self.LeafImage.url
    #     except:
    #         url = ''
    #     return url
    
