from django.db import models
from datetime import datetime,date
from django.db.models.fields import (DateTimeField,DurationField,DateField,TimeField,EmailField,)
# Create your models here.
class Item(models.Model):
    name=models.CharField(max_length=25)
    profile=models.ImageField(upload_to='pics')
    img1=models.ImageField(upload_to='pics' ,null=True )
    img2=models.ImageField(upload_to='pics' ,null=True )
    img3=models.ImageField(upload_to='pics' ,null=True )
    img4=models.ImageField(upload_to='pics' ,null=True )
    short_description=models.CharField(max_length=50)
    long_description=models.TextField()
    basePrice=models.IntegerField()
    currentPrice=models.IntegerField()
    
    tag=models.CharField(max_length=25)
    
    status=models.CharField(null=True,max_length=25)
    
    sold=models.CharField(max_length=10,default="unsold")
    
    ownermail = models.EmailField(unique=False)
    start_date=models.DateField()
    highest_bidder=models.IntegerField(null=True)

    sendwinmail = models.CharField(max_length=7,default="unsended")