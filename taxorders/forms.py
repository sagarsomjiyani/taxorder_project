# taxorders/forms.py
from django import forms
from .models import TaxOrder, CertificateConsumption, ContractMaster

class CertificateForm(forms.ModelForm):
    class Meta:
        model = TaxOrder
        fields = ['company_code','contract_number','vendor_code','vendor_name','certificate_number', 'certificate_date', 'certificate_amount', 'tds_section_code', 'tax_order_section', 'tax_rate']

class ConsumptionForm(forms.ModelForm):
    class Meta:
        model = CertificateConsumption
        fields = '__all__' 

class ContractForm(forms.ModelForm):
    class Meta:
        model = ContractMaster
        fields = '__all__' 