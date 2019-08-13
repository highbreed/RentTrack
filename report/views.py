from django.shortcuts import render, get_object_or_404
from .models import Invoice
from .forms import InvoiceForm
from core.models import LEASE


def home_view(request):
    invoices_qs = Invoice.objects.all()
    form = InvoiceForm()
    context = {
        "invoice": invoices_qs,
        'form': form,
    }

    return render(request, 'report_base.html', context)

def generate_invoice(request):
    if request.method == 'GET':
        form = InvoiceForm()
    elif request.method == 'POST':
        # todo: add toaster message
        form = InvoiceForm(initial=request.POST)
        if form.is_valid():
            form.save()
            form = InvoiceForm()
    existing_invoices = Invoice.objects.all()
    context = {'form': form,}
    return render(request, 'invoice_form.html', context)


def check_invoices(request):
    invoices_qs = Invoice.objects.all()
    context = {
        "invoice": invoices_qs
    }

    return render(request, 'invoice_display.html', context)


def display_invoice(request, slug):
    """
    get all time entries for a project and date range, and generate a invoice.
    Expected query parameters:
      - invoiceId
    """
    if request.method == 'GET':
        invoice = get_object_or_404(Invoice, slug=slug)
        lease_qs = LEASE.objects.get(unit_id=invoice.unit)

        context = {
            'tenant': lease_qs.tenant_id,
            'start': invoice.start,
            'unit': invoice.unit,
            'end': invoice.end,
            'invoice_date': invoice.date,
            'price': lease_qs.rent,
            'property': lease_qs.property_id,
            'invoice_items': invoice.unit,
            'description': invoice.description,

        }

        return render(request, 'invoice_detail.html', context)


