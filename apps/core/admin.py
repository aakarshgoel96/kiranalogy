from django.contrib import admin

from apps.core.models import *


admin.site.register(Store)
admin.site.register(Vendor)
admin.site.register(Product)
admin.site.register(PurchaseBill)
admin.site.register(PurchaseDetail)
admin.site.register(SellBill)
admin.site.register(SellDetail)
