from contextlib import redirect_stderr
from multiprocessing import context
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
    
    context ={
        
    }


    return render(request,'cash_flow_summary.html',context)