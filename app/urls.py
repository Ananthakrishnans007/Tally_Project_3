from django.urls import path
from . import views

urlpatterns = [
    path('',views.Index,name='Index'),

    path('cash_flow',views.cash_flow,name='cash_flow'),

    path('cash_flow_summary/<int:id>',views.cash_flow_summary,name='cash_flow_summary'),

    path('group_cash_flow/<int:id>',views.group_cash_flow,name='group_cash_flow'),


    path('group_cash_flow_2/<int:id>',views.group_cash_flow_2,name='group_cash_flow_2'),

    path('ledger_vouchers/<int:id>',views.ledger_vouchers,name='ledger_vouchers'),

    path('delete/<int:id>/<int:pk>',views.delete,name='delete'),

     path('test',views.test,name='test'),




    


    

    




    



    path('test',views.test,name='test'),



   


    

    

  
]
