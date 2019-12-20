from django.db import models

# Create your models here.
class info(models.Model):
    title=models.CharField(max_length=30)
    headertext=models.CharField(max_length=50,default='sample')
    card1head = models.CharField(max_length=50,blank=True,default='sample')
    card2head = models.CharField(max_length=50,blank=True,default='sample')
    card3head = models.CharField(max_length=50,blank=True,default='sample')
    card4head = models.CharField(max_length=50,blank=True,default='sample')
    card1cont = models.CharField(max_length=50,blank=True,default='sample')
    card2cont = models.CharField(max_length=50,blank=True,default='sample')
    card3cont = models.CharField(max_length=50,blank=True,default='sample')
    card4cont = models.CharField(max_length=50,blank=True,default='sample')
    address=models.CharField(max_length=100,blank=True,default='sample')
    number=models.CharField(max_length=15,blank=True,default='sample')
    emailid=models.CharField(max_length=50,blank=True,default='sample')

    def __str__(self):
        return self.title

  
    