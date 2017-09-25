from django.contrib.auth.models import User
from django_extensions.db.models import TimeStampedModel
from django.db import models


class Store(TimeStampedModel):
    owner = models.ForeignKey(User)
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=20, unique=True)
    address_line_1 = models.CharField(max_length=50)
    address_line_2 = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.CharField(max_length=6)
    contact = models.CharField(max_length=10)

    def __unicode__(self):
        return "{0}-{1}-{2}".format(self.owner, self.name, self.code)


class Product(TimeStampedModel):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=20, unique=True)
    category = models.CharField(max_length=10)
    sub_category = models.CharField(max_length=10)

    def __unicode__(self):
        return "{0}-{1}".format(self.name, self.code)


class Vendor(TimeStampedModel):
    store = models.ForeignKey(Store)
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=20, unique=True)
    address_line_1 = models.CharField(max_length=50)
    address_line_2 = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.CharField(max_length=6)
    contact = models.CharField(max_length=10)

    def __unicode__(self):
        return "{0}-{1}".format(self.name, self.code)


class PurchaseBill(TimeStampedModel):
    store = models.ForeignKey(Store)
    vendor = models.ForeignKey(Vendor)
    bill_no = models.PositiveIntegerField()
    billing_date = models.DateTimeField()
    total_discount = models.FloatField(default=0)
    total_tax = models.FloatField(default=0)
    total_amount = models.FloatField()
    total_payable_amount = models.FloatField()

    def __unicode__(self):
        return "{0}-{1}".format(self.vendor, self.bill_no)


class PurchaseDetail(TimeStampedModel):
    bill = models.ForeignKey(PurchaseBill)
    product = models.ForeignKey(Product)
    discount_per_unit = models.FloatField(default=0)
    tax_per_unit = models.FloatField(default=0)
    unit_price = models.FloatField()
    mrp = models.FloatField()
    quantity = models.PositiveIntegerField()
    expiry_date = models.DateField()

    def __unicode__(self):
        return "{0}-{1}".format(self.bill, self.product)


class SellBill(TimeStampedModel):
    store = models.ForeignKey(Store)
    customer_name = models.CharField(max_length=50)
    bill_no = models.PositiveIntegerField()
    billing_date = models.DateTimeField()
    total_discount = models.FloatField(default=0)
    total_tax = models.FloatField(default=0)
    total_amount = models.FloatField()
    total_payable_amount = models.FloatField()

    def __unicode__(self):
        return "{0}-{1}".format(self.customer_name, self.bill_no)


class SellDetail(TimeStampedModel):
    bill = models.ForeignKey(SellBill)
    product = models.ForeignKey(Product)
    discount_per_unit = models.FloatField(default=0)
    tax_per_unit = models.FloatField(default=0)
    mrp = models.FloatField()
    quantity = models.PositiveIntegerField()
    expiry_date = models.DateField(blank=True, null=True)

    def __unicode__(self):
        return "{0}-{1}".format(self.bill, self.product)
