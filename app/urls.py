from django.urls import path
from . import views

urlpatterns = [
    path('',views.Index,name='Index'),

    path('cash_flow',views.cash_flow,name='cash_flow'),

    path('cash_flow_summary/<int:id>',views.cash_flow_summary,name='cash_flow_summary'),

    path('group_cash_flow/<int:id>',views.group_cash_flow,name='group_cash_flow'),


    path('group_cash_flow_2/<int:id>',views.group_cash_flow_2,name='group_cash_flow_2'),

    path('cashflow_ledger_vouchers/<int:id>',views.cashflow_ledger_vouchers,name='cashflow_ledger_vouchers'),

    path('cashflow_vouchers_delete/<int:id>/<int:pk>',views.cashflow_vouchers_delete,name='cashflow_vouchers_delete'),

  


    


    

  
]
