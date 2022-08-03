from django.db import models

# Create your models here.

# class Position(models.Model):
#     title = models.CharField(max_length=50)

    # def __str__(self):
    #     return self.title

class db(models.Model):
    WO = models.CharField(max_length=20)
    Com = models.CharField(max_length=20)
    CMS= models.CharField(max_length=15)
    Status = models.CharField(max_length=20)
    CUName = models.CharField(max_length=20)
    Scope= models.CharField(max_length=15)
    R_T = models.CharField(max_length=20)
    Smart_req= models.CharField(max_length=10)
    smart=models.CharField(max_length=10)
    Address = models.CharField(max_length=50)
    Proc_req=models.CharField(max_length=15)
    Proc_id = models.CharField(max_length=10)
    Abbr_req = models.CharField(max_length=10)
    Abbr_id = models.CharField(max_length=10)
    Host_req = models.CharField(max_length=10)
    #position= models.ForeignKey(Position,on_delete=models.CASCADE)
    
