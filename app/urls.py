from django.urls import path
from . import views

urlpatterns = [
    path('',views.Index,name='Index'),

    path('cash_flow',views.cash_flow,name='cash_flow'),

    path('cash_flow_summary',views.cash_flow_summary,name='cash_flow_summary'),


    

    

  
]
