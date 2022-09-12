from django.contrib import admin

from . models import*

# Register your models here.

admin.site.register(Months)

admin.site.register(Ledger)

admin.site.register(Groups)

admin.site.register(Group_inflow_outflow)

admin.site.register(Sub_Group)

admin.site.register(Sub)

admin.site.register(Ledger_inflow_outflow)

admin.site.register(Ledger_Vouchers)





