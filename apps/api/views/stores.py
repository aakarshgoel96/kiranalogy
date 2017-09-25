from rest_framework.viewsets import ModelViewSet

from apps.api.serializers import stores as stores_serializer
from apps.core.models import stores as stores_models


class StoreViewSet(ModelViewSet):
    queryset = stores_models.Store.objects.all()
    serializer_class = stores_serializer.StoreSerializer


class VendorViewSet(ModelViewSet):
    queryset = stores_models.Vendor.objects.all()
    serializer_class = stores_serializer.VendorSerializer


class ProductViewSet(ModelViewSet):
    queryset = stores_models.Product.objects.all()
    serializer_class = stores_serializer.ProductSerializer


class PurchaseBillViewSet(ModelViewSet):
    queryset = stores_models.PurchaseBill.objects.all()
    serializer_class = stores_serializer.PurchaseBillSerializer


class PurchaseDetailViewSet(ModelViewSet):
    queryset = stores_models.PurchaseDetail.objects.all()
    serializer_class = stores_serializer.PurchaseDetailSerializer


class SellBillViewSet(ModelViewSet):
    queryset = stores_models.SellBill.objects.all()
    serializer_class = stores_serializer.SellBillSerializer


class SellDetailViewSet(ModelViewSet):
    queryset = stores_models.SellDetail.objects.all()
    serializer_class = stores_serializer.SellDetailSerializer
