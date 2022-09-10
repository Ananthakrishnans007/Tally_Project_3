from django.urls import path
from . import views

urlpatterns = [
    path('',views.Index,name='Index'),

    path('cash_flow',views.cash_flow,name='cash_flow'),

    path('cash_flow_summary',views.cash_flow_summary,name='cash_flow_summary'),

    path('group_cash_flow',views.group_cash_flow,name='group_cash_flow'),


    path('group_cash_flow_2',views.group_cash_flow_2,name='group_cash_flow_2'),

    path('ledger_vouchers',views.ledger_vouchers,name='ledger_vouchers'),


    

    




    



    path('test',views.test,name='test'),



   


    

    

  
]
