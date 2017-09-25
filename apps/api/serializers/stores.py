from rest_framework.serializers import ModelSerializer

from apps.core.models import *


class StoreSerializer(ModelSerializer):
    
    class Meta:
        model = Store


class VendorSerializer(ModelSerializer):

    class Meta:
        model = Vendor


class ProductSerializer(ModelSerializer):

    class Meta:
        model = Product


class PurchaseBillSerializer(ModelSerializer):

    class Meta:
        model = PurchaseBill


class PurchaseDetailSerializer(ModelSerializer):

    class Meta:
        model = PurchaseDetail


class SellBillSerializer(ModelSerializer):

    class Meta:
        model = SellBill


class SellDetailSerializer(ModelSerializer):

    class Meta:
        model = SellDetail
