from django.db import models

# Create your models here.



class Months(models.Model):
    month_name= models.CharField(max_length=255)

    def __str__(self):
        return self.month_name 




class Ledger(models.Model):
    Ledger_name = models.CharField(max_length=255)
    Opening_balance = models.IntegerField(blank=True,null=True)
    Type = models.CharField(max_length=255,default='Dr',blank=True,null=True)    

    def __str__(self):
        return self.Ledger_name   

class Groups(models.Model):
    Group_name = models.CharField(max_length=255)
    def __str__(self):
        return self.Group_name
class Group_inflow_outflow(models.Model):
    Group = models.ForeignKey(Groups,on_delete=models.CASCADE)
    Amount = models.IntegerField()
    Type = models.CharField(max_length=255,blank=True,null=True)

    def __str__(self):
        return self.Group.Group_name




  
