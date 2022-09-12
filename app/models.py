from django.db import models

# Create your models here.



class Months(models.Model):
    month_name= models.CharField(max_length=255)

    def __str__(self):
        return self.month_name 




class Ledger(models.Model):
    Ledger_name = models.CharField(max_length=255)
    Opening_balance = models.IntegerField(blank=True,null=True)
    Type = models.CharField(max_length=255,blank=True,null=True)    

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

class Sub_Group(models.Model):
    Sub_Group_name = models.CharField(max_length=255) 

    def __str__(self):
        return self.Sub_Group_name

class Sub(models.Model):
    Group = models.ForeignKey(Group_inflow_outflow,on_delete=models.CASCADE)
    Sub_group = models.ForeignKey(Sub_Group,on_delete=models.CASCADE)    
    Amount = models.IntegerField()
    Type = models.CharField(max_length=255,blank=True,null=True)
    def __str__(self):
        return self.Sub_group.Sub_Group_name

class Ledger_inflow_outflow(models.Model):
    sub = models.ForeignKey(Sub,on_delete=models.CASCADE)
    Ledger=models.ForeignKey(Ledger,on_delete=models.CASCADE)
    Amount = models.IntegerField()
    Type = models.CharField(max_length=255,blank=True,null=True)
    def __str__(self):
        return self.Ledger.Ledger_name     

class Ledger_Vouchers(models.Model):
    Ledger_inflow_outflow = models.ForeignKey(Ledger_inflow_outflow,on_delete=models.CASCADE)
    Date = models.DateField()
    Particulars = models.ForeignKey(Ledger,on_delete=models.CASCADE)
    Vch_Type = models.CharField(max_length=255)
    Vch_No = models.IntegerField()
    Debit =models.IntegerField(blank=True,null=True)
    Credit = models.IntegerField(blank=True,null=True)
    Type = models.CharField(max_length=255,blank=True,null=True)

    def __str__(self):
        return self.Ledger_inflow_outflow.Ledger.Ledger_name     












  
