import rest_framework_filters as drf_filters

from apps.core.models import *


__all__ = [
    'UserFilterSet', 'StoreFilterSet', 'VendorFilterSet', 'ProductFilterSet', 'PurchaseBillFilterSet',
    'PurchaseDetailFilterSet', 'SellBillFilterSet', 'SellDetailFilterSet'
]


class PurchaseDetailFilterSet(drf_filters.FilterSet):
    class Meta:
        model = PurchaseDetail


class SellDetailFilterSet(drf_filters.FilterSet):

    class Meta:
        model = SellDetail


class SellBillFilterSet(drf_filters.FilterSet):
    selldetail = drf_filters.RelatedFilter(SellDetailFilterSet)

    class Meta:
        model = SellBill


class PurchaseBillFilterSet(drf_filters.FilterSet):
    purchasedetail = drf_filters.RelatedFilter(PurchaseDetailFilterSet)

    class Meta:
        model = PurchaseBill


class UserFilterSet(drf_filters.FilterSet):

    class Meta:
        model = User


class VendorFilterSet(drf_filters.FilterSet):
    purchasebill = drf_filters.RelatedFilter(PurchaseBillFilterSet)

    class Meta:
        model = Vendor


class StoreFilterSet(drf_filters.FilterSet):
    vendor = drf_filters.RelatedFilter(VendorFilterSet)
    purchasebill = drf_filters.RelatedFilter(PurchaseBillFilterSet)
    sellbill = drf_filters.RelatedFilter(SellBillFilterSet)

    class Meta:
        model = Store


class ProductFilterSet(drf_filters.FilterSet):
    purchasedetail = drf_filters.RelatedFilter(PurchaseDetailFilterSet)
    selldetail = drf_filters.RelatedFilter(SellDetailFilterSet)

    class Meta:
        model = Product


