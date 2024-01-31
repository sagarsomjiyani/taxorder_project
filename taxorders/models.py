# taxorders/models.py
from django.db import models
from django.contrib.auth.models import User

class TaxOrder(models.Model):
    company_code = models.CharField(max_length=3)
    contract_number = models.CharField(max_length=255)
    vendor_code = models.CharField(max_length=6)
    vendor_name = models.CharField(max_length=255)
    certificate_number = models.CharField(max_length=10)
    certificate_date = models.DateField()
    certificate_amount = models.DecimalField(max_digits=15, decimal_places=2)
    tds_section_code = models.CharField(max_length=4)
    tax_order_section = models.CharField(max_length=3)
    tax_rate = models.DecimalField(max_digits=5, decimal_places=2)
    consumed = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    balance = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    sectioncode = models.CharField(max_length=3,default="CP")
    fiscalyear =models.IntegerField(default=2023, max_length=4)

class CertificateConsumption(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tax_order = models.ForeignKey(TaxOrder, on_delete=models.CASCADE)
    document_number = models.CharField(max_length=10, default=0000000000)
    consumption_amount = models.DecimalField(max_digits=10, decimal_places=2)

class ContractMaster(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ola_number = models.IntegerField(max_length=10, default=0000000000)
    vendor_code = models.IntegerField(max_length=6, default=000000)
    vendor_name = models.CharField(max_length=255)
    vendor_address = models.CharField(max_length=255, default="address")
    payment_currency = models.CharField(choices={"USD":"USD","JPY":"JPY","EUR":"EUR","AED":"AED"}, max_length=3)
    payment_bank = models.CharField(max_length=255)
    payment_swift = models.CharField(max_length=255)
    payment_iban = models.CharField(max_length=255)
    payment_inter = models.CharField(choices={"Yes":"Yes","No":"No"}, max_length=3)    
    payment_ibank = models.CharField(max_length=255)
    payment_iswift = models.CharField(max_length=255)
    payment_iiban = models.CharField(max_length=255)