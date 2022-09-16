from calendar import month
from django.db import models

# Create your models here.



class Months(models.Model):
    month_name= models.CharField(max_length=255)

    def __str__(self):
        return self.month_name 




class Ledger1(models.Model):
    ledger_name = models.CharField(max_length=255)
    ledger_opening_bal = models.IntegerField(blank=True,null=True)
    ledger_type = models.CharField(max_length=255,blank=True,null=True)    

    def __str__(self):
        return self.ledger_name   

class cash_flow_Groups(models.Model):
    Group_name = models.CharField(max_length=255)
    def __str__(self):
        return self.Group_name
class Group_inflow_outflow(models.Model):
    Group = models.ForeignKey(cash_flow_Groups,on_delete=models.CASCADE)
    Amount = models.IntegerField(default=0,blank=True,null=True)
    Type = models.CharField(max_length=255,blank=True,null=True)
    month = models.ForeignKey(Months,on_delete=models.CASCADE)

    def __str__(self):
        return self.Group.Group_name

class cash_flow_Sub_Group(models.Model):
    Sub_Group_name = models.CharField(max_length=255) 

    def __str__(self):
        return self.Sub_Group_name

class cash_flow_Sub(models.Model):
    Group = models.ForeignKey(Group_inflow_outflow,on_delete=models.CASCADE)
    Sub_group = models.ForeignKey(cash_flow_Sub_Group,on_delete=models.CASCADE)    
    Amount = models.IntegerField(default=0,blank=True,null=True)
    Type = models.CharField(max_length=255,blank=True,null=True)


    def __str__(self):
        return self.Sub_group.Sub_Group_name

class Ledger_inflow_outflow(models.Model):
    sub = models.ForeignKey(cash_flow_Sub,on_delete=models.CASCADE)
    Ledger=models.ForeignKey(Ledger1,on_delete=models.CASCADE)
    Amount = models.IntegerField(default=0,blank=True,null=True)
    Type = models.CharField(max_length=255,blank=True,null=True)

    def __str__(self):
        return self.Ledger.ledger_name    

class cash_flow_Ledger_Vouchers(models.Model):
    Ledger_inflow_outflow = models.ForeignKey(Ledger_inflow_outflow,on_delete=models.CASCADE)
    Date = models.DateField()
    Particulars = models.ForeignKey(Ledger1,on_delete=models.CASCADE)
    Vch_Type = models.CharField(max_length=255)
    Vch_No = models.IntegerField()
    Debit =models.IntegerField(blank=True,null=True)
    Credit = models.IntegerField(blank=True,null=True)
    Type = models.CharField(max_length=255,blank=True,null=True)

    def __str__(self):
        return self.Ledger_inflow_outflow.Ledger.ledger_name

class Cash_Flow(models.Model):
    Inflow =models.IntegerField(blank=True,null=True)
    Outflow =models.IntegerField(blank=True,null=True)
    NetFlow =models.IntegerField(blank=True,null=True)
    month = models.ForeignKey(Months,on_delete=models.CASCADE)

    def __str__(self):
        return self.month


    













  
