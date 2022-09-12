from contextlib import redirect_stderr
from multiprocessing import context
from tokenize import group
from unicodedata import name
from django.shortcuts import render,redirect

from . models import*

# Create your views here.


def Index(request):
    return render(request,'index.html')

# cash flow
    
def cash_flow(request):
    mo = Months.objects.all()
    context ={
        'mo' :mo
    }


    return render(request,'cash_flow.html',context)


def cash_flow_summary(request):
    group = Group_inflow_outflow.objects.all()

    total_inflow=0
    total_outflow=0
    for i in group:
        if i.Type == 'Inflow':
            total_inflow += i.Amount
        else:
            total_outflow += i.Amount
    net_flow =total_inflow - total_outflow

    context ={
        'group':group,
        'total_inflow' :total_inflow,
        'total_outflow':total_outflow,
        'net_flow':net_flow,
        
    }


    return render(request,'cash_flow_summary.html',context)



def group_cash_flow(request,id):
    group=Group_inflow_outflow.objects.get(id=id)
    type =group.Type
    


    sub_group = Sub.objects.filter(Group=id)

    total=0
    for i in sub_group:
        total +=i.Amount
    context ={
        'group':group,
        'sub_group':sub_group,
        'total':total,
        'type':type,
    }

    return render(request,'group_cash_flow.html',context)



def group_cash_flow_2(request,id):
    sub =Sub.objects.get(id=id)
    ledger = Ledger_inflow_outflow.objects.filter(sub=id)
    total =0
    for i in ledger:
        total += i.Amount


    
    context ={
        'sub':sub,
        'ledger':ledger,
        'total':total,
    }

    return render(request,'group_cash_flow_2.html',context)
   

def ledger_vouchers(request,id):
    ledger = Ledger_inflow_outflow.objects.get(Ledger=id)
    ledger_vouchers = Ledger_Vouchers.objects.filter(Ledger_inflow_outflow=ledger)

    
    for i in ledger_vouchers:
        if ledger.Type=="Inflow":
            if i.Vch_Type == 'Receipt' or 'Sales':
                i.Type = 'Inflow'
                i.save()
        else:
            if i.Vch_Type == 'Payment' or 'Purchase':
                i.Type = 'Outflow'
                i.save()


    



    context ={
        'ledger':ledger ,
        'ledger_vouchers':ledger_vouchers
    }

    return render(request,'ledger_vouchers.html',context)
   





def test(request):
    return render(request,'test.html')
