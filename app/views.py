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


def cash_flow_summary(request,id):
    group = Group_inflow_outflow.objects.filter(month=id)
    
    

    total_inflow=0
    total_outflow=0
    for i in group:
        if i.Type == 'Inflow':
            total_inflow += i.Amount
        else:
            total_outflow += i.Amount
    net_flow =total_inflow - total_outflow
    if net_flow == -net_flow:
        net_flow = -1* net_flow

    mo = Months.objects.get(id = id)

    if Flow .objects.filter(month=id):
        f = Flow .objects.get(month=id)
        f.Inflow = total_inflow
        f.Outflow =total_outflow
        f.NetFlow = net_flow

        f.month = mo
        f.save()
    else:
        f = Flow ()
        f.Inflow = total_inflow
        f.Outflow =total_outflow
        f.NetFlow = net_flow

        f.month = mo
        f.save()    


    
    


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

    group1=Group_inflow_outflow.objects.get(id=id) 
    group1.Amount =  total
    group1.save()

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
    total = 0
    for i in ledger:
        total += i.Amount

    sub1 =Sub.objects.get(id=id)
    sub1.Amount = total 
    sub1.save()


    
    context ={
        'sub':sub,
        'ledger':ledger,
        'total':total,
    }

    return render(request,'group_cash_flow_2.html',context)
   

def ledger_vouchers(request,id):
    ledger = Ledger_inflow_outflow.objects.get(Ledger=id)
    
    ledger_vouchers = Ledger_Vouchers.objects.filter(Ledger_inflow_outflow=ledger)
    
    total_debit = 0
    total_credit = 0
    for i in ledger_vouchers:
        if ledger.Type=="Inflow":

            if i.Vch_Type == 'Receipt' or 'Sales':
                i.Type = 'Inflow'
                i.save()
        else:
            
            if i.Vch_Type == 'Payment' or 'Purchase':
                i.Type = 'Outflow'
                i.save()

    for j in ledger_vouchers:
        if j.Debit:
            total_debit +=j.Debit
        if j.Credit:
            total_credit +=j.Credit

    if ledger.Type =='Inflow':
        le = Ledger_inflow_outflow.objects.get(Ledger=id)
        le.Amount = total_credit
        le.save()
    else:
        le = Ledger_inflow_outflow.objects.get(Ledger=id)
        le.Amount = total_debit
        le.save()





    



    context ={
        'ledger':ledger ,
        'ledger_vouchers':ledger_vouchers,
        'total_debit':total_debit,
        'total_credit':total_credit,

    }

    return render(request,'ledger_vouchers.html',context)
   




def delete(request, id,pk):
    post = Ledger_Vouchers.objects.get(id=id)
    post.delete()
    return redirect(ledger_vouchers,pk)
  
def test(request):
    
    ledger_vouchers = Ledger_Vouchers.objects.all

    context ={
        'ledger_vouchers'  :ledger_vouchers ,
    }

    return render(request,'test.html',context)
