from django import forms
from .models import SalesInvoice, SalesInvoiceEntry
from invoicing.forms import InvoiceForm

class SalesInvoiceForm(InvoiceForm):
    class Meta(InvoiceForm.Meta):
        model = SalesInvoice
        labels = {
            'discount': 'Discount %'
        }


class SalesInvoiceEntryForm(forms.ModelForm):

    discount = forms.DecimalField(max_digits=12, decimal_places=2, initial=0)

    def save(self, *args, **kwargs):
        self.instance.price = self.instance.product.sale_price-self.cleaned_data["discount"]
        return super().save(*args, **kwargs)

    def clean(self):
        
        cleaned_data = super().clean()

        discount = cleaned_data.get('discount')
        sale_price = cleaned_data.get('product').sale_price
        minimum_price = cleaned_data.get('product').minimum_price

        if minimum_price > sale_price-discount:
            self.add_error('discount', 'Discount too high!')

    class Meta:
        model = SalesInvoiceEntry
        exclude = ['invoice', 'price']
