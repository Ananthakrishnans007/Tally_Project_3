from contextlib import redirect_stderr
from multiprocessing import context
from tokenize import group
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



def group_cash_flow(request):
    context ={
        
    }

    return render(request,'group_cash_flow.html',context)



def group_cash_flow_2(request):
    context ={
        
    }

    return render(request,'group_cash_flow_2.html',context)
   

def ledger_vouchers(request):
    context ={
        
    }

    return render(request,'ledger_vouchers.html',context)
   





def test(request):
    return render(request,'test.html')
