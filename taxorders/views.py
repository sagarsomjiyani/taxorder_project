# taxorders/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import TaxOrder, CertificateConsumption
from .forms import CertificateForm, ConsumptionForm

@login_required
def tax_order_list(request):
    company_code_filter = request.GET.get('company_code_filter', '')
    contract_number_filter = request.GET.get('contract_number_filter', '')
    vendor_code_filter = request.GET.get('vendor_code_filter', '')

    tax_orders = TaxOrder.objects.filter(
        company_code__icontains=company_code_filter,
        contract_number__icontains=contract_number_filter,
        vendor_code__icontains=vendor_code_filter
    )

    return render(request, 'taxorders/tax_order_list.html', {
        'tax_orders': tax_orders,
        'company_code_filter': company_code_filter,
        'contract_number_filter': contract_number_filter,
        'vendor_code_filter': vendor_code_filter,
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
    return render(request, 'taxorders/tax_order_detail.html', {'tax_order': tax_order})
