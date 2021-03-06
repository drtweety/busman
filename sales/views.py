from django.urls import reverse_lazy
from .models import SalesInvoice, SalesInvoiceEntry, SALE
from .filters import SalesInvoiceFilter
from .forms import SalesInvoiceForm, SalesInvoiceEntryForm

from invoicing.views import (
    InvoiceListView,
    InvoiceCreateView, 
    InvoiceDetailView, 
    InvoiceUpdateView, 
    InvoiceDeleteView,
    InvoiceEntryCreateView,
    InvoiceEntryDeleteView)

# Create your views here.
class SalesInvoiceListView(InvoiceListView):
    model = SalesInvoice
    filterset_class = SalesInvoiceFilter
    template_name = "sales/salesinvoice_list.html"


class SalesInvoiceCreateView(InvoiceCreateView):
    model = SalesInvoice
    form_class = SalesInvoiceForm

class SalesInvoiceDetailView(InvoiceDetailView):
    model = SalesInvoice
    finalize_action = SALE
    invoice_finalize_redirect_name = 'sales-view'

class SalesInvoiceUpdateView(InvoiceUpdateView):
    model = SalesInvoice
    form_class = SalesInvoiceForm
   
class SalesInvoiceDeleteView(InvoiceDeleteView):
    model = SalesInvoice
    success_url = reverse_lazy('sales-list')

class SalesInvoiceEntryCreateView(InvoiceEntryCreateView):
    model = SalesInvoiceEntry
    parent_model = SalesInvoice
    action = SalesInvoice.SALE
    form_class = SalesInvoiceEntryForm
        

class SalesInvoiceEntryDeleteView(InvoiceEntryDeleteView):
    model = SalesInvoiceEntry

class SalesInvoicePrintView(InvoiceDetailView):
    model = SalesInvoice
    template_name = 'sales/salesinvoice_print.html'