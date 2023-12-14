from django.db import models

# Create your models here.

class member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
class member_list(models.Model):
    length = models.DateField()
    member = models.ForeignKey('member', on_delete= models.CASCADE)