from django.contrib import admin

from . models import*

# Register your models here.

admin.site.register(Months)

admin.site.register(Ledger)

admin.site.register(Groups)

admin.site.register(Group_inflow_outflow)



