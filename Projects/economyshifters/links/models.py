from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User



class Links(models.Model):  #Admin needs to add links here in this model with default referral id
    
    name=models.CharField(max_length=200)
    description=models.TextField()
    link=models.URLField()
    default_referral=models.CharField(max_length=200)
    frequency=models.CharField(max_length=5, blank=True)
    category = models.ForeignKey('categories.Category')
    def __str__(self):
        return self.name

    

class Link_Info(models.Model):     #Users info going to be updated here
    user=models.ForeignKey(User,unique=False)
    link=models.ForeignKey(Links,unique=False)
    referral_id=models.CharField(max_length=200)
    

class User_refferal(models.Model):
    Main_user=models.ForeignKey(User,unique=True,related_name="primary_user")
    Referred_user=models.ForeignKey(User,unique=False)





