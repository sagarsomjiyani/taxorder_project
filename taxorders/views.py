# taxorders/views.py
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import login_required
from .models import TaxOrder, CertificateConsumption, ContractMaster
from .forms import CertificateForm, ConsumptionForm, ContractForm

@login_required
def tax_order_list(request):
    company_code_filter = request.GET.get('company_code_filter', '')
    contract_number_filter = request.GET.get('contract_number_filter', '')
    vendor_code_filter = request.GET.get('vendor_code_filter', '')
    vendor_name_filter = request.GET.get('vendor_name_filter', '')
    fiscalyear_filter = request.GET.get('fiscalyear_filter', '')
    sectioncode_filter = request.GET.get('sectioncode_filter', '')
    tax_orders = TaxOrder.objects.filter(
        fiscalyear__icontains=fiscalyear_filter,
        company_code__icontains=company_code_filter,
        contract_number__icontains=contract_number_filter,
        vendor_code__icontains=vendor_code_filter,
        vendor_name__icontains=vendor_name_filter,
        sectioncode__icontains=sectioncode_filter
    )

    return render(request, 'taxorders/tax_order_list.html', {
        'tax_orders': tax_orders,
        'company_code_filter': company_code_filter,
        'contract_number_filter': contract_number_filter,
        'vendor_code_filter': vendor_code_filter,
        'vendor_name_filter': vendor_name_filter,
        'sectioncode_filter': sectioncode_filter,
        'fiscalyear_filter': fiscalyear_filter,

    })

@login_required
def add_certificate(request):
    if request.method == 'POST':
        form = CertificateForm(request.POST)
        if form.is_valid():
            certificate = form.save()
            return redirect('tax_order_list')
    else:
        form = CertificateForm()

    return render(request, 'taxorders/add_certificate.html', {'form': form})

@login_required
def enter_consumption(request, tax_order_id):
    tax_order = TaxOrder.objects.get(pk=tax_order_id)

    if request.method == 'POST':
        form = ConsumptionForm(request.POST)
        if form.is_valid():
            consumption = form.save(commit=False)
            consumption.tax_order = tax_order
            consumption.user = request.user
            consumption.save()
            # Update the tax order's consumed and balance fields
            tax_order.consumed += consumption.consumption_amount
            tax_order.balance = tax_order.certificate_amount - tax_order.consumed
            tax_order.save()
            return redirect('tax_order_list')
    else:
        form = ConsumptionForm()

    return render(request, 'taxorders/enter_consumption.html', {'form': form, 'tax_order': tax_order})

@login_required
def tax_order_detail(request, tax_order_id):
    tax_order = get_object_or_404(TaxOrder, pk=tax_order_id)
    tax_order_cons = list(CertificateConsumption.objects.filter(tax_order=tax_order.id))
    if tax_order_cons != "":
        tax_order_consd = tax_order_cons
    else:
        tax_order_consd = ""
    return render(request, 'taxorders/tax_order_detail.html', {'tax_order': tax_order,'tax_order_cons': tax_order_consd})

@login_required
def add_contract(request):
    if request.method == 'POST':
        form = ContractForm(request.POST)
        if form.is_valid():
            contract = form.save(commit=False)
            contract.user = request.user
            contract.save()
            return redirect('tax_order_list')
    else:
        form = ContractForm()

    return render(request, 'taxorders/add_contract.html', {'form': form})

@login_required
def contract_details_list(request):
    ola_number_filter = request.GET.get('ola_number_filter', '')
    vendor_code_filter = request.GET.get('vendor_code_filter', '')
    payment_currency_filter = request.GET.get('payment_currency_filter', '')
    contracts = ContractMaster.objects.filter(
        ola_number__icontains=ola_number_filter,
        vendor_code__icontains=vendor_code_filter,
        payment_currency__icontains=payment_currency_filter
    )
    if contracts != "":
        contracts = contracts
    else:
        contracts = ""

    return render(request, 'taxorders/contract_details_list.html', {
        'contracts': contracts,
        'ola_number_filter': ola_number_filter,
        'payment_currency_filter': payment_currency_filter,
        'vendor_code_filter': vendor_code_filter,

    })